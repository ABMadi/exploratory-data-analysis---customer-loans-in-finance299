import pandas as pd
import matplotlib.pyplot as plt
import os

# Use forward slashes for the file path
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v5_with_instalment_and_total_rec_prncp.csv'

# Load the final dataset
loan_data_cleaned = pd.read_csv(file_path)

# Create the directory for visualisations in 03_Data_Analysis if it doesn't exist
visualisations_dir = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/03_Data_Analysis/visualisations/'
os.makedirs(visualisations_dir, exist_ok=True)

# Step 1: Calculate percentage of loans recovered
loan_data_cleaned['percentage_recovered'] = (loan_data_cleaned['total_rec_prncp'] / loan_data_cleaned['loan_amount']) * 100

# Summarise the percentage recovered across all loans
average_percentage_recovered = loan_data_cleaned['percentage_recovered'].mean()
print(f"Average Percentage of Loans Recovered: {average_percentage_recovered:.2f}%")

# Step 2: Calculate amount to be paid back in 6 months with interest
loan_data_cleaned['payment_in_6_months'] = loan_data_cleaned['instalment'] * 6

# Step 3: Visualise Results

# Visualise the percentage of loans recovered
plt.figure(figsize=(10, 6))
plt.hist(loan_data_cleaned['percentage_recovered'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Percentage of Loans Recovered")
plt.xlabel("Percentage Recovered")
plt.ylabel("Frequency")
plt.grid(True)
# Save before displaying
plt.savefig('C:/Users/user/Documents/AiCore/Projects/Finance_Project/03_Data_Analysis/visualisations/percentage_recovered.png')
plt.show()

# Visualise the amount expected to be paid in 6 months
plt.figure(figsize=(10, 6))
plt.hist(loan_data_cleaned['payment_in_6_months'], bins=20, color='lightgreen', edgecolor='black')
plt.title("Amount Expected to Be Paid in 6 Months")
plt.xlabel("Amount ($)")
plt.ylabel("Frequency")
plt.grid(True)
# Save before displaying
plt.savefig('C:/Users/user/Documents/AiCore/Projects/Finance_Project/03_Data_Analysis/visualisations/payments_in_6_months.png')
plt.show()

# Save the results
output_file = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_summary.csv'
loan_data_cleaned.to_csv(output_file, index=False)
print(f"Summary data saved to: {output_file}")
