import pandas as pd
import matplotlib.pyplot as plt
import os

# Use forward slashes for the file path
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v5_with_instalment_and_total_rec_prncp.csv'

# Load the final dataset
loan_data_cleaned = pd.read_csv(file_path)

# Step 1: Identify Charged Off Loans
charged_off_loans = loan_data_cleaned[loan_data_cleaned['loan_status'] == 'Charged Off'].copy()

# Step 2: Calculate expected revenue for each loan
# Extract numeric value from the 'term' column and multiply by the monthly installment
charged_off_loans.loc[:, 'expected_revenue'] = charged_off_loans['term'].str.extract(r'(\d+)')[0].astype(int) * charged_off_loans['instalment']

# Step 3: Calculate the loss (expected revenue - total payment received so far)
charged_off_loans.loc[:, 'loss'] = charged_off_loans['expected_revenue'] - charged_off_loans['total_payment']

# Step 4: Summarize the total loss across all charged off loans
total_loss = charged_off_loans['loss'].sum()
print(f"Total Expected Loss from Charged Off Loans: ${total_loss:,.2f}")

# Step 5: Add the total expected loss to the beginning of the CSV
# Create a DataFrame for the summary row
summary_data = pd.DataFrame({
    'id': ['Summary'],
    'loan_amount': [''],
    'instalment': [''],
    'expected_revenue': [f"Total Expected Loss: ${total_loss:,.2f}"],
    'total_payment': [''],
    'loss': ['']
})

# Concatenate the summary row with the charged off loans data
charged_off_summary = pd.concat([summary_data, charged_off_loans[['id', 'loan_amount', 'instalment', 'expected_revenue', 'total_payment', 'loss']]])

# Save the combined DataFrame to a CSV file
output_file = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/charged_off_loss_summary.csv'
charged_off_summary.to_csv(output_file, index=False)

# Step 6: Visualize the loss projected over the remaining term of the loans
plt.figure(figsize=(10, 6))
plt.bar(charged_off_loans['id'], charged_off_loans['loss'], color='salmon', edgecolor='black')
plt.title('Projected Loss from Charged Off Loans')
plt.xlabel('Loan ID')
plt.ylabel('Projected Loss ($)')
plt.xticks(rotation=90)
plt.grid(True)

# Save the plot
output_dir = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/03_Data_Analysis/visualisations/'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f'{output_dir}/projected_loss_charged_off_loans.png')

plt.show()

print(f"Charged off loans summary with loss saved to: {output_file}")
