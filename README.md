# Caprae AI-Readiness Pre-Screening: Lead Enrichment Tool

## Project Overview

This project provides a robust solution for enhancing sales leads by automatically enriching them with valuable information extracted from company websites. Specifically, it identifies official LinkedIn company page URLs and generates concise website summaries for each lead, enabling sales and marketing teams to gain quick, actionable insights.

Beyond core enrichment, this tool includes a dedicated visualization module that provides insightful charts and tables, making it easier to analyze the quality of the enriched data and identify trends within the lead list. Developed with a focus on reproducibility and best practices, this project is ideal for data professionals looking to automate lead qualification processes.

## Features

* **Automated Lead Enrichment:** Scrapes company websites to find associated LinkedIn company page URLs.
* **Website Summarization:** Extracts and condenses key information (title, meta description, H1 tags) from company homepages into a concise summary.
* **CSV-Based Workflow:** Reads input leads from a CSV file and outputs enriched data to another CSV file.
* **Robust Web Scraping:** Utilizes `requests` for fetching web content and `BeautifulSoup` for efficient HTML parsing, with error handling for network issues and missing content.
* **Data Visualization:** Generates various plots to visualize:
    * The success rate of LinkedIn URL discovery by industry.
    * The distribution of leads across different industries.
    * Common keywords found in website summaries (Word Cloud).
    * Data completeness and missing values across all columns.
* **Reproducible Environment:** Uses a `requirements.txt` file to manage and ensure consistent installation of all Python dependencies.

## Project Structure
         caprae_leadgen_challenge/                 
         ├── data/                      
         │   ├── input_leads.csv        
         │   └── output_enriched_leads.csv
         ├── images/                    
         │   ├── companies_per_industry.png
         │   ├── linkedin_success_by_industry.png
         │   ├── missing_data_bar.png
         │   ├── missing_data_matrix.png
         │   └── website_summary_wordcloud.png
         ├── src/                     
         │   ├── init.py           
         │   ├── enricher.py          
         │   └── main.py               
         ├── README.md              
         ├── analysis.md    
         ├── caprae_research.md
         ├── report.md
         ├── requirements.txt        
         └── visualize_output.py       
## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* **Python 3.8+**: Download and install from [python.org](https://www.python.org/downloads/).
* **Git**: For cloning the repository. Download from [git-scm.com](https://git-scm.com/downloads).
* **Visual Studio Code (VS Code)** or your preferred IDE/text editor.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yTheSwaroop/caprae_leadgen_challenge.git](https://github.com/TheSwaroop/caprae_leadgen_challenge.git)
    ```
2.  **Navigate to the Project Directory:**
    ```bash
    cd caprae_leadgen_challenge
    ```
3.  **Create a Virtual Environment (Recommended):**
    A virtual environment isolates your project's dependencies from your system's Python packages.
    ```bash
    python -m venv .venv
    ```
4.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **On macOS / Linux:**
        ```bash
        source ./.venv/bin/activate
        ```
    (Your terminal prompt should now show `(.venv)` at the beginning, indicating the environment is active.)

5.  **Install Dependencies:**
    Install all required Python packages listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Prepare Input Data

Place your lead data in a CSV file (e.g., `input_leads.csv`) inside the `data/` directory. The CSV **must** contain at least two columns: `Company Name` and `Website`. An example `input_leads.csv` is provided.

### 2. Run the Lead Enrichment Tool

Execute the main script to process your input leads and generate the enriched output CSV.

```bash
python -m src.main --input data/input_leads.csv --output data/output_enriched_leads.csv
--input: Path to your input CSV file.

--output: Path where the enriched CSV will be saved (defaults to data/output_enriched_leads.csv).

The script will print progress updates to the console.

3. Generate Visualizations
Once output_enriched_leads.csv is generated, you can run the visualization script to get insights.

Bash

python visualize_output.py
This script will:

Print enhanced tabular views of the enriched data to the console.

Generate and display several plots (which will also be saved as .png files in the project root):

linkedin_success_by_industry.png: Bar chart showing LinkedIn discovery rates.

companies_per_industry.png: Bar chart of company counts per industry.

website_summary_wordcloud.png: Word cloud of common terms in summaries.

missing_data_matrix.png & missing_data_bar.png: Visualizations of data completeness.

Output & Insights
The output_enriched_leads.csv file will contain all your original input columns, plus two new columns:

LinkedIn URL: The discovered LinkedIn company page URL, or empty if not found.

Website Summary: A concise summary (up to 250 characters) extracted from the company's homepage.

The generated visualizations provide quick insights:

LinkedIn Success Rate: Helps identify which industries or types of companies are more likely to have discoverable LinkedIn profiles.

Industry Distribution: Shows the composition of your lead list by industry.

Website Summary Word Cloud: Offers a high-level overview of the products, services, or themes prevalent across your lead companies based on their homepage content.

Missing Data Visualizations: Crucial for understanding the quality and completeness of your enriched data, indicating where the tool was unable to find specific information.

Contributing
Feel free to fork this repository, open issues, or submit pull requests. Suggestions for improvements and new features are welcome!

Contact
For any questions or feedback, please contact:
[Your Swaroop Raparthi/raparthiswaroop6300@gmail.com/https://www.linkedin.com/in/raparthi-swaroop-342405358/] 
