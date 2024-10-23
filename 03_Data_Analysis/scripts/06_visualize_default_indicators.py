import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths for loading data
categorical_comparison_file = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/categorical_comparisons.csv'
indicator_correlation_file = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/indicator_correlation_summary.csv'

# Load the data
categorical_comparison_df = pd.read_csv(categorical_comparison_file)
indicator_correlation_summary_df = pd.read_csv(indicator_correlation_file)

# Create the directory for saving visualisations if it doesn't exist
save_dir = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/01_Results/Comparison_Results'
os.makedirs(save_dir, exist_ok=True)

# Set up the style for the plots
sns.set(style="whitegrid")

# Plot 1: Comparison of Home Ownership between Charged Off and At Risk
plt.figure(figsize=(6, 4))
sns.barplot(x='status', y='MORTGAGE', data=categorical_comparison_df)
plt.title("Comparison of Home Ownership (MORTGAGE) Between Charged Off and At-Risk Customers")
plt.savefig(f'{save_dir}/home_ownership_comparison.png')
plt.show()

# Plot 2: Comparison of Loan Grades
plt.figure(figsize=(6, 4))
sns.barplot(x='status', y='RENT', data=categorical_comparison_df)
plt.title("Comparison of Loan Grades (RENT) Between Charged Off and At-Risk Customers")
plt.savefig(f'{save_dir}/loan_grades_comparison.png')
plt.show()

# Plot 3: DTI Comparison (from indicator correlation summary)
plt.figure(figsize=(6, 4))
sns.barplot(x='status', y='dti', data=indicator_correlation_summary_df)
plt.title("Comparison of DTI Between Charged Off and At-Risk Customers")
plt.savefig(f'{save_dir}/dti_comparison.png')
plt.show()

# Plot 4: Comparison of Outstanding Principal
plt.figure(figsize=(6, 4))
sns.barplot(x='status', y='out_prncp', data=indicator_correlation_summary_df)
plt.title("Comparison of Outstanding Principal Between Charged Off and At-Risk Customers")
plt.savefig(f'{save_dir}/out_prncp_comparison.png')
plt.show()

# Plot 5: Comparison of Total Payment
plt.figure(figsize=(6, 4))
sns.barplot(x='status', y='total_payment', data=indicator_correlation_summary_df)
plt.title("Comparison of Total Payment Between Charged Off and At-Risk Customers")
plt.savefig(f'{save_dir}/total_payment_comparison.png')
plt.show()
