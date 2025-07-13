# Caprae AI-Readiness Pre-Screening: Lead Enrichment Tool

# 🚀 Project Overview

This project delivers an automated solution to transform raw sales leads into actionable intelligence. By scraping company websites, it extracts official LinkedIn company URLs and generates concise website summaries, directly enhancing lead qualification and sales outreach efficiency. It includes powerful visualization tools to assess data quality and uncover valuable business insights from your enriched leads.

# ✨ Key Features

* **Automated Lead Enrichment:** Efficiently discovers LinkedIn company page URLs from provided website links.
* **Concise Website Summaries:** Generates short (up to 250 characters) business summaries from website content (titles, meta descriptions, H1s).
* **CSV-Driven Workflow:** Seamlessly processes `.csv` input files and outputs enriched data to a new `.csv`.
* **Robust Web Scraping:** Built with `requests` and `BeautifulSoup` for reliable web content extraction, including error handling.
* **Comprehensive Data Visualization:** Creates insightful charts (e.g., LinkedIn discovery rates, industry distribution, missing data analysis, word clouds) saved as `.png` files.

## Prerequisites

- Python 3.8+
- Required libraries: Install dependencies using the following command:

```bash
pip install -r requirements.txt
```

Ensure you have a CSV file with at least the following columns in the `data/` directory:
- `company_name`: The name of the company.
- `industry`: The industry the company belongs to.
- `website`: The company's website URL.

## Usage

### 1. Prepare Input Data
Place your input CSV file (e.g., `data/input_leads.csv`) in the `data/` directory with the required columns (`company_name`, `industry`, `website`). Additional columns are preserved in the output.

### 2. Run the Enrichment Script
To enrich your lead data with LinkedIn URLs and website summaries, run the following command from the project root:

```bash
python src/enrich_leads.py --input data/input_leads.csv --output data/output_enriched_leads.csv
```

- `--input`: Path to your input CSV file (e.g., `data/input_leads.csv`).
- `--output`: Path where the enriched CSV will be saved (defaults to `data/output_enriched_leads.csv`).

The script will print progress updates to the console.

### 3. Generate Visualizations
After generating `data/output_enriched_leads.csv`, run the visualization script from the project root:

```bash
python visualize_output.py
```

This script will:
- Print enhanced tabular views of the enriched data to the console.
- Generate and save the following plots as `.png` files in the `images/` directory:
* **Input Data Distribution:**
    * As shown in the "Number of Companies per Industry in Leads" chart, the sample primarily consisted of SaaS companies (3 leads), followed by CRM, Communication, and Project Management (2 leads each), and various other industries with single leads. This diversity provides a good test case for the enrichment logic across different business types.
    * All 19 input leads had complete 'Company Name', 'Website', and 'Industry' fields, providing a solid foundation for enrichment.

    ![Number of Companies per Industry in Leads](images/companies_per_industry.png)

* **Enrichment Completeness:**
    * The "Completeness of Columns in Enriched Leads" bar chart and "Missing Data Matrix of Enriched Leads" visually confirm that the tool successfully enriched **10 out of 19 leads** (approximately 53%) with both 'LinkedIn URL' and 'Website Summary'. This indicates a strong success rate for automated discovery, considering the inherent variability of website structures and external link presence.

    ![Completeness of Columns in Enriched Leads](images/missing_data_bar.png)
    ![Missing Data Matrix of Enriched Leads](images/missing_data_matrix.png)

* **LinkedIn URL Discovery by Industry:**
    * The "Percentage of LinkedIn URLs Found by Industry" chart highlights variations in LinkedIn discovery rates across industries. Industries like 'AI Writing Assistant', 'Project Management', 'Marketing', 'Low-code', 'Forms & Surveys', and 'Fintech' showed 100% success in finding LinkedIn URLs for their respective companies in the sample.
    * 'SaaS' (the largest category) achieved a success rate of approximately 65%, while 'Communication' was around 45%. This indicates that while the tool is generally effective, the discoverability of LinkedIn profiles can vary based on industry-specific web practices or individual company web development choices. Industries with lower success (e.g., 'CRM', 'Design', 'E-commerce' at 0% in this sample) may require further investigation into their specific web structures or an expansion of the scraping logic to alternative discovery methods.

    ![Percentage of LinkedIn URLs Found by Industry](images/linkedin_success_by_industry.png)

* **Website Summary Insights:**
    * The "Common Keywords in Website Summaries" word cloud visually represents the most common keywords extracted from the generated website summaries. Prominent terms like "work," "app," "innovation," "platform," "marketing," "tool," "email," "team," "build," "free," "revenue," "workflows," "automation," and "CRM" clearly indicate that the summaries successfully captured the essence of companies operating within the technology, SaaS, and business solutions sectors. This confirms the utility of the `get_website_summary` function in providing quick, relevant business context.

    ![Common Keywords in Website Summaries](images/website_summary_wordcloud.png)

## Visualizations

The `visualize_output.py` script produces several insightful plots to analyze the enriched data, saved in the `images/` directory.

### LinkedIn URL Success Rate by Industry
A bar chart showing the percentage of companies with successfully found LinkedIn URLs, broken down by industry. This helps understand data completeness across sectors.

### Number of Companies per Industry
A bar chart displaying the distribution of companies across industries in your lead list.

### Common Keywords in Website Summaries
A word cloud generated from website summaries, with larger words indicating higher frequency. This provides a quick visual summary of common themes and business areas.

### Missing Data Visualizations
These plots, generated using the `missingno` library, visualize data completeness.

#### Missing Data Matrix
A matrix showing missing values (white spaces) across all columns, useful for identifying patterns in incomplete data.

#### Completeness of Columns
A bar chart quantifying the percentage of non-missing values per column, offering a clear overview of data quality and enrichment success.

## Output & Key Insights

The `data/output_enriched_leads.csv` file will include all original input columns plus two new columns:
- `LinkedIn URL`: The discovered LinkedIn company page URL, or empty if not found.
- `Website Summary`: A concise summary (up to 250 characters) extracted from the company's homepage.

The generated visualizations provide the following insights:
- **LinkedIn Success Rate**: Identifies industries with higher discoverable LinkedIn profiles.
- **Industry Distribution**: Shows the composition of your lead list by industry.
- **Website Summary Word Cloud**: Highlights prevalent products, services, or themes.
- **Missing Data Visualizations**: Indicates the quality and completeness of enriched data.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests. Suggestions for improvements and new features are welcome!

## Contact

For questions, feedback, or collaborations, please reach out:

- **Swaroop Raparthi**
- **Email**: raparthiswaroop6300@gmail.com
- **LinkedIn**: [Swaroop Raparthi](https://www.linkedin.com/in/raparthi-swaroop-342a85358/)
- **GitHub**: [TheSwaroop](https://github.com/TheSwaroop)
