# Caprae AI-Readiness Pre-Screening: Lead Enrichment

This project provides a Python-based tool to enrich a CSV file containing company leads with LinkedIn URLs and website summaries, and generate insightful visualizations to analyze the enriched data. Last updated: 04:06 PM IST, Sunday, July 13, 2025.

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
  - `images/linkedin_success_by_industry.png`: Bar chart showing LinkedIn discovery rates.
  - `images/companies_per_industry.png`: Bar chart of company counts per industry.
  - `images/website_summary_wordcloud.png`: Word cloud of common keywords in website summaries.
  - `images/missing_data_matrix.png`: Visualization of data completeness.
  - `images/missing_data_bar.png`: Bar chart of column completeness.

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

## License

This project is open-sourced under the MIT License. See the `LICENSE` file in the repository root for details.

## Contact

For questions, feedback, or collaborations, please reach out:

- **Swaroop Raparthi**
- **Email**: raparthiswaroop6300@gmail.com
- **LinkedIn**: [Swaroop Raparthi](https://www.linkedin.com/in/raparthi-swaroop-342a85358/)
- **GitHub**: [TheSwaroop](https://github.com/TheSwaroop)