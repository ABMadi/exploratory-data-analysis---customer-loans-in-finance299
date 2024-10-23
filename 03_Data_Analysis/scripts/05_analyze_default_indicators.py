import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Use forward slashes for the file path
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v5_with_instalment_and_total_rec_prncp.csv'

# Load the final dataset
loan_data_cleaned = pd.read_csv(file_path)

# Check available columns
print("Available columns:", loan_data_cleaned.columns)

# Step 1: Subset the data for Charged Off and At-Risk customers
charged_off_customers = loan_data_cleaned[loan_data_cleaned['loan_status'] == 'Charged Off'].copy()
at_risk_customers = loan_data_cleaned[loan_data_cleaned['loan_status'].str.contains('Late', na=False)].copy()

# Combine both sets into one DataFrame for easy comparison
charged_off_customers['status'] = 'Charged Off'
at_risk_customers['status'] = 'At Risk'
combined_data = pd.concat([charged_off_customers, at_risk_customers])

# Step 2: Analyze potential indicators
# Checking correlations of numeric features against 'status'
available_numeric_features = ['loan_amount', 'annual_inc', 'dti', 'employment_length', 
                              'open_accounts', 'total_accounts', 'out_prncp', 
                              'total_payment', 'recoveries']

correlations = {}
for feature in available_numeric_features:
    if feature in combined_data.columns:
        # Compare mean values of numeric features between Charged Off and At-Risk customers
        feature_mean = combined_data.groupby('status')[feature].mean()
        print(f"\nComparison of {feature} between Charged Off and At-Risk Customers:")
        print(feature_mean)
        correlations[feature] = feature_mean
    else:
        print(f"Feature {feature} not found in the dataset.")

# Step 3: Visualize Indicators
sns.set(style="whitegrid")

# Create a 'Comparison' subfolder in the visualisations directory
output_dir = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/03_Data_Analysis/visualisations/Comparison/'
os.makedirs(output_dir, exist_ok=True)

# Visualize correlation of each feature for Charged Off and At-Risk customers
for feature in available_numeric_features:
    if feature in combined_data.columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=combined_data, x='status', y=feature)
        plt.title(f'Comparison of {feature} Between Charged Off and At-Risk Customers')
        plt.grid(True)
        
        # Save each plot in the 'Comparison' subfolder
        plt.savefig(f'{output_dir}/{feature}_comparison.png')
        plt.show()

# Step 4: Summary of Correlations (Optional)
correlation_summary = pd.DataFrame(correlations)
correlation_summary.to_csv('C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/indicator_correlation_summary.csv')
print("Correlation summary saved to: C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/indicator_correlation_summary.csv")

# Optional: Save comparisons of categorical columns
categorical_features = ['grade', 'purpose', 'home_ownership']
for feature in categorical_features:
    if feature in combined_data.columns:
        comparison = combined_data.groupby(['status', feature]).size().unstack()
        plt.figure(figsize=(10, 6))
        comparison.plot(kind='bar', stacked=True, colormap='viridis', edgecolor='black')
        plt.title(f'Comparison of {feature} Between Charged Off and At-Risk Customers')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.grid(True)
        plt.xticks(rotation=90 if feature == 'purpose' else 0)
        
        # Save the categorical comparison plot in the 'Comparison' subfolder
        plt.savefig(f'{output_dir}/{feature}_categorical_comparison.png')
        plt.show()

# Save comparison data for categorical columns to CSV
comparison_summary = pd.concat([comparison for feature in categorical_features], keys=categorical_features)
comparison_summary.to_csv('C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/categorical_comparisons.csv')
print("Categorical comparisons saved to: C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/categorical_comparisons.csv")
