import argparse
# Use a relative import for enricher if main.py and enricher.py are in the same package (folder)
# The '.' indicates the current package/directory.
# In src/main.py
from .enricher import enrich_leads_from_csv # This is the relative import

def main():
    """
    Main function to parse arguments and initiate the lead enrichment process.
    """
    parser = argparse.ArgumentParser(
        description="Lead Enrichment Tool: Adds LinkedIn Company URLs to leads by scraping their websites."
    )
    parser.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help="Path to the input CSV file containing leads (e.g., data/input_leads.csv). "
             "Must have 'Company Name' and 'Website' columns."
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='data/output_enriched_leads.csv', # Default output path
        help="Path to the output CSV file for enriched leads (default: data/output_enriched_leads.csv)."
    )

    args = parser.parse_args()

    print("\n--- Lead Enrichment Tool Started ---")
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")

    # Call the enrichment function from the enricher module
    enrich_leads_from_csv(args.input, args.output)

    print("\n--- Lead Enrichment Tool Finished ---")

if __name__ == '__main__':
    main()