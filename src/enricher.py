import requests
from bs4 import BeautifulSoup
import re
import csv
import time

def get_website_content(url):
    """
    Fetches the HTML content of a given URL.
    Includes basic headers to mimic a browser and a timeout.
    """
    try:
        # Add headers to avoid some basic bot detection
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        # Attempt to get the URL, with a 10-second timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.Timeout:
        print(f"  Timeout while fetching {url}. Skipping.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"  Error fetching {url}: {e}. Skipping.")
        return None

def find_linkedin_url_on_page(html_content):
    """
    Parses HTML content to find a LinkedIn company page URL.
    Prioritizes direct links to company pages, then general LinkedIn links if specific not found.
    """
    if not html_content:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    linkedin_url = None

    # --- Strategy 1: Look for <a> tags with 'linkedin.com/company/' ---
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Use regex for more flexible matching
        match = re.search(r'https?://(?:www\.)?linkedin\.com/(?:company|companies)/[a-zA-Z0-9_-]+(?:/?(?:[?#][\S]*)?)?', href)
        if match:
            linkedin_url = match.group(0).split('?')[0].split('#')[0] # Clean up URL
            break # Found a company link, prioritize and stop

    # --- Strategy 2: Look for LinkedIn patterns in general text/script tags ---
    # This is a fallback if no direct <a> tag is found.
    # It might catch URLs embedded in JavaScript or other text.
    if not linkedin_url:
        # Search in the full text content and also in script tags
        content_to_search = soup.get_text(separator=' ', strip=True) + str(soup.find_all('script'))
        
        # Broader regex to catch /company/, /in/ (profile), /pub/ (old profile), /groups/, /showcase/
        # We'll prioritize /company/ or /companies/ if found.
        matches = re.finditer(r'https?://(?:www\.)?linkedin\.com/(?:company|companies|in|pub|groups|showcase)/[a-zA-Z0-9_-]+(?:/?(?:[?#][\S]*)?)?', content_to_search, re.IGNORECASE)
        
        # Prioritize company pages
        temp_linkedin_url = None
        for match in matches:
            found_url = match.group(0).split('?')[0].split('#')[0] # Clean up URL parameters/fragments
            if '/company/' in found_url.lower() or '/companies/' in found_url.lower():
                linkedin_url = found_url # Found a specific company page, this is best
                break
            elif '/in/' in found_url.lower() and not temp_linkedin_url:
                # Store first found /in/ as a fallback, but keep looking for /company/
                temp_linkedin_url = found_url

        if not linkedin_url and temp_linkedin_url: # If no company page, but a profile was found
            linkedin_url = temp_linkedin_url

    return linkedin_url

def get_website_summary(html_content):
    """
    Extracts a concise summary of the website's content, focusing on title, meta description, and H1.
    """
    if not html_content:
        return "" # Return empty string if no content

    soup = BeautifulSoup(html_content, 'html.parser')
    
    summary_parts = []

    # 1. Page Title
    if soup.title and soup.title.string:
        summary_parts.append(soup.title.string.strip())

    # 2. Meta Description
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if meta_description and meta_description.get('content'):
        summary_parts.append(meta_description['content'].strip())

    # 3. Main Heading (H1) - often a prominent tagline or main product/service
    main_heading = soup.find('h1')
    if main_heading:
        summary_parts.append(main_heading.get_text(separator=' ', strip=True))
    
    # Combine unique parts and clean up extra spaces
    # Use a set to maintain uniqueness, then join
    # Using dict.fromkeys to preserve order while making items unique, then convert to list for join
    combined_summary = " ".join(list(dict.fromkeys(summary_parts)))
    combined_summary = re.sub(r'\s+', ' ', combined_summary).strip() # Replace multiple spaces with single space

    # Limit to a reasonable length for the CSV cell to avoid excessively long strings
    return combined_summary[:250] # Return first 250 characters as a concise summary

def enrich_lead(lead):
    """
    Enriches a single lead dictionary with 'LinkedIn URL' and 'Website Summary' keys
    by attempting to find them on the company's website.
    """
    company_name = lead.get('Company Name', '').strip()
    website = lead.get('Website', '').strip()

    lead['LinkedIn URL'] = ''       # Initialize with empty string
    lead['Website Summary'] = ''    # Initialize new field with empty string

    if not website:
        print(f"Skipping enrichment for '{company_name}' due to missing website.")
        return lead

    # Prepare URLs to try (http and https versions)
    if not website.startswith(('http://', 'https://')):
        test_urls = [f'https://{website}', f'http://{website}']
    else:
        test_urls = [website]

    found_useful_info = False # Flag to track if any info (LinkedIn OR Summary) was found
    
    for url_to_fetch in test_urls:
        print(f"\n  Attempting to fetch {url_to_fetch} for '{company_name}'...")
        html = get_website_content(url_to_fetch)
        
        if html:
            # --- Extract LinkedIn URL ---
            linkedin_url = find_linkedin_url_on_page(html)
            if linkedin_url:
                lead['LinkedIn URL'] = linkedin_url
                print(f"  --> Found LinkedIn: {linkedin_url}")
                found_useful_info = True
            else:
                print(f"  No LinkedIn URL found on {url_to_fetch}.")

            # --- Extract Website Summary ---
            website_summary = get_website_summary(html)
            if website_summary:
                lead['Website Summary'] = website_summary
                # Truncate for display in console, but full summary is in 'lead' dict
                print(f"  --> Website Summary: '{website_summary[:70]}...'") 
                found_useful_info = True
            else:
                print(f"  No meaningful website summary found on {url_to_fetch}.")
            
            # If we successfully fetched content from this URL and found *something* useful,
            # we can stop trying other protocol versions.
            if found_useful_info: 
                break 
        else:
            print(f"  Could not retrieve content from {url_to_fetch}.")

    if not lead['LinkedIn URL']: # Check if LinkedIn URL was *not* found after all attempts
        print(f"  Final: No LinkedIn URL found for '{company_name}'.")
    if not lead['Website Summary']: # Check if Website Summary was *not* found after all attempts
        print(f"  Final: No Website Summary found for '{company_name}'.")

    time.sleep(1) # Be polite to websites
    return lead

def enrich_leads_from_csv(input_filepath, output_filepath):
    """
    Reads leads from an input CSV, enriches them, and writes
    the enriched data to a new output CSV.
    """
    leads_data = []
    fieldnames = []

    try:
        with open(input_filepath, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames # Get original headers from input CSV
            if not fieldnames:
                print(f"Error: Input CSV '{input_filepath}' is empty or has no headers.")
                return

            leads_data = list(reader)
            print(f"Loaded {len(leads_data)} leads from '{input_filepath}'.")

            # Basic check for required columns
            if 'Company Name' not in fieldnames or 'Website' not in fieldnames:
                print("Warning: 'Company Name' or 'Website' column not found in input CSV. Results may be limited.")

            enriched_leads = []
            for i, lead in enumerate(leads_data):
                print(f"\nProcessing lead {i + 1}/{len(leads_data)}: {lead.get('Company Name', 'N/A')}")
                enriched_leads.append(enrich_lead(lead))

            # --- CRITICAL PART: Ensure new columns are in the output fieldnames ---
            # Create a set of existing fieldnames for quick lookup
            existing_fieldnames_set = set(fieldnames) 

            # Add 'LinkedIn URL' if not already present
            if 'LinkedIn URL' not in existing_fieldnames_set:
                fieldnames.append('LinkedIn URL')
            
            # Add 'Website Summary' if not already present
            if 'Website Summary' not in existing_fieldnames_set: # <--- THIS IS THE KEY LINE
                fieldnames.append('Website Summary')
            # --- END CRITICAL PART ---

        with open(output_filepath, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader() # Write the header row
            writer.writerows(enriched_leads) # Write all enriched rows
        print(f"\n--- Enrichment complete! Results saved to '{output_filepath}' ---")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_filepath}'. Please ensure the path is correct.")
    except Exception as e:
        print(f"An unexpected error occurred during CSV processing: {e}")

if __name__ == '__main__':
    print("This is the enricher module. Run main.py to use the tool.")