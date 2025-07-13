import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import missingno as msno
from tabulate import tabulate
import os

# --- Configuration ---
OUTPUT_CSV_PATH = 'data/output_enriched_leads.csv'

# --- 1. Load Data ---
print("--- Loading Enriched Data ---")
if not os.path.exists(OUTPUT_CSV_PATH):
    print(f"Error: Output CSV not found at '{OUTPUT_CSV_PATH}'. Please run 'python -m src.main' first.")
    exit()

try:
    df = pd.read_csv(OUTPUT_CSV_PATH)
    print(f"Successfully loaded {len(df)} leads from '{OUTPUT_CSV_PATH}'.")
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit()

# --- 2. Tabular Visualization (Enhanced Display) ---
print("\n--- 2.1 Enriched Leads Data (Pandas Full Display) ---")
# Set Pandas display options for better console output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1200) # Increased width for more columns
pd.set_option('display.colheader_justify', 'left')
pd.set_option('display.max_colwidth', 100) # Limit column width for readability

# Print the DataFrame using .to_string() to avoid console truncation
print(df.to_string())

print("\n--- 2.2 Enriched Leads Data (Tabulated for Console) ---")
# Convert DataFrame to a list of lists (excluding header)
table_data = df.values.tolist()
headers = df.columns.tolist()
print(tabulate(table_data, headers=headers, tablefmt="grid"))


# --- 3. Diagrams and Charts (Visualizing Insights) ---

# Prepare data for LinkedIn success rate
df['LinkedIn Found'] = df['LinkedIn URL'].apply(lambda x: True if pd.notna(x) and x != '' else False)

# 3.1 Bar Chart: LinkedIn URL Success Rate by Industry
if 'Industry' in df.columns:
    print("\n--- 3.1 Generating Bar Chart: LinkedIn URL Success Rate by Industry ---")
    # Calculate percentage of LinkedIn found per industry
    linkedin_success_by_industry = df.groupby('Industry')['LinkedIn Found'].value_counts(normalize=True).unstack(fill_value=0)

    # Ensure 'True' column exists (for found)
    if True in linkedin_success_by_industry.columns:
        plt.figure(figsize=(12, 7))
        # Sort by percentage found for better visualization
        plot_data = linkedin_success_by_industry[True].sort_values(ascending=False)
        sns.barplot(x=plot_data.values, y=plot_data.index, palette='viridis')
        plt.title('Percentage of LinkedIn URLs Found by Industry', fontsize=16)
        plt.xlabel('Percentage Found', fontsize=12)
        plt.ylabel('Industry', fontsize=12)
        plt.xlim(0, 1) # Ensure x-axis goes from 0 to 1 (for percentage)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('linkedin_success_by_industry.png') # Save the plot
        plt.show()
    else:
        print("No LinkedIn URLs were found for any industry to plot success rate.")
else:
    print("Skipping LinkedIn URL Success Rate by Industry chart: 'Industry' column not found.")


# 3.2 Bar Chart: Top Industries in Your Lead List
if 'Industry' in df.columns:
    print("\n--- 3.2 Generating Bar Chart: Number of Companies per Industry ---")
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, y='Industry', order=df['Industry'].value_counts().index, palette='coolwarm')
    plt.title('Number of Companies per Industry in Leads', fontsize=16)
    plt.xlabel('Number of Companies', fontsize=12)
    plt.ylabel('Industry', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('companies_per_industry.png') # Save the plot
    plt.show()
else:
    print("Skipping Top Industries chart: 'Industry' column not found.")


# 3.3 Word Cloud: Common Keywords in Website Summaries
print("\n--- 3.3 Generating Word Cloud: Common Keywords in Website Summaries ---")
# Filter out empty summaries before joining
all_summaries = ' '.join(df['Website Summary'].dropna().tolist())

if all_summaries:
    wordcloud = WordCloud(width=800, height=400, background_color='white', collocations=False).generate(all_summaries)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Common Keywords in Website Summaries', fontsize=16)
    plt.tight_layout()
    plt.savefig('website_summary_wordcloud.png') # Save the plot
    plt.show()
else:
    print("No website summaries available to generate a word cloud.")


# 3.4 Missing Data Visualization (using missingno)
print("\n--- 3.4 Generating Missing Data Visualizations ---")
plt.figure(figsize=(10, 6))
msno.matrix(df, figsize=(10, 6), color=(0.2, 0.4, 0.6), sparkline=False)
plt.title('Missing Data Matrix of Enriched Leads', fontsize=16)
plt.tight_layout()
plt.savefig('missing_data_matrix.png') # Save the plot
plt.show()

plt.figure(figsize=(10, 6))
msno.bar(df, figsize=(10, 6), color='lightgreen')
plt.title('Completeness of Columns in Enriched Leads', fontsize=16)
plt.tight_layout()
plt.savefig('missing_data_bar.png') # Save the plot
plt.show()

print("\n--- Visualization process complete! Check your project directory for saved plots. ---")