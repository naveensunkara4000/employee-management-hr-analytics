import os
import pandas as pd
from src.data_loader import load_hr_data
from src.preprocessing import basic_cleaning
from src.eda import plot_attrition_by_department, correlation_heatmap
import matplotlib.pyplot as plt

# -------------------------------
# Define paths
# -------------------------------

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")
OUTPUT_FILE = os.path.join(REPORTS_DIR, "output.txt")

PROCESSED_DATA = os.path.join(PROCESSED_DIR, "hr_analytics_clean.csv")

# Make sure folders exist
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)


# Create required folders
os.makedirs(FIGURES_DIR, exist_ok=True)

# -------------------------------
# Step 1: Load Data
# -------------------------------

print("Loading dataset...")
df = load_hr_data()

# -------------------------------
# Step 2: Clean Data
# -------------------------------

print("Cleaning dataset...")
df_clean = basic_cleaning(df)

df_clean.to_csv(PROCESSED_DATA, index=False)
print(f"Cleaned dataset saved to: {PROCESSED_DATA}")

# -------------------------------
# Step 3: Generate Visualizations
# -------------------------------

print("Generating plots...")

plt.figure()
plot_attrition_by_department(df_clean)
plt.savefig(os.path.join(FIGURES_DIR, "attrition_by_department.png"))
plt.close()

plt.figure()
correlation_heatmap(df_clean)
plt.savefig(os.path.join(FIGURES_DIR, "correlation_heatmap.png"))
plt.close()

print(f"Plots saved in: {FIGURES_DIR}")

# -------------------------------
# Step 4: Generate Text Summary
# -------------------------------

summary_text = f"""
EMPLOYEE MANAGEMENT HR ANALYTICS REPORT
---------------------------------------

Total Rows: {len(df_clean)}
Total Columns: {len(df_clean.columns)}

Missing Values After Cleaning: {df_clean.isna().sum().sum()}

Departments:
{df_clean['Department'].value_counts().to_string()}

Attrition Rate:
{df_clean['Attrition'].value_counts(normalize=True) * 100}
"""

with open(OUTPUT_FILE, "w") as f:
    f.write(summary_text)

print(f"Report generated at: {OUTPUT_FILE}")

print("\n✓ Project executed successfully!")
