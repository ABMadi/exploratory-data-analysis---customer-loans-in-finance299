import pandas as pd
import os

# Use forward slashes for the file path
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v5_with_instalment_and_total_rec_prncp.csv'

# Load the final dataset
loan_data_cleaned = pd.read_csv(file_path)

# Step 1: Identify Charged Off Loans
charged_off_loans = loan_data_cleaned[loan_data_cleaned['loan_status'] == 'Charged Off']

# Step 2: Calculate percentage of Charged Off loans
total_loans = len(loan_data_cleaned)
charged_off_count = len(charged_off_loans)
percentage_charged_off = (charged_off_count / total_loans) * 100
print(f"Percentage of Charged Off Loans: {percentage_charged_off:.2f}%")

# Step 3: Calculate total amount paid towards Charged Off loans before charge off
total_paid_before_chargeoff = charged_off_loans['total_payment'].sum()  # Assuming 'total_payment' represents payments made
print(f"Total Amount Paid Towards Charged Off Loans Before Charge Off: ${total_paid_before_chargeoff:,.2f}")

# Step 4: Create the summary DataFrame first
summary_data = {
    'id': ['Summary', 'Summary'],
    'loan_amount': ['', ''],
    'total_payment': [f"Percentage Charged Off: {percentage_charged_off:.2f}%", 
                      f"Total Paid Before Charge Off: ${total_paid_before_chargeoff:,.2f}"]
}

summary_df = pd.DataFrame(summary_data)

# Concatenate the summary DataFrame with the charged off loans DataFrame
combined_df = pd.concat([summary_df, charged_off_loans[['id', 'loan_amount', 'total_payment']]])

# Step 5: Save the combined DataFrame to the CSV file
output_file = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/charged_off_summary.csv'
combined_df.to_csv(output_file, index=False)
print(f"Charged off loan summary and analysis saved to: {output_file}")
