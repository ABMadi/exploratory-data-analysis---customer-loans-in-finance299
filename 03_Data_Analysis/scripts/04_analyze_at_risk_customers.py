import pandas as pd
import matplotlib.pyplot as plt
import os

# Use forward slashes for the file path
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v5_with_instalment_and_total_rec_prncp.csv'

# Load the final dataset
loan_data_cleaned = pd.read_csv(file_path)

# Step 1: Identify customers who are behind on payments
# Filter customers with 'Late' status (assuming 'Late (31-120 days)' and 'Late (16-30 days)' are indicators)
at_risk_customers = loan_data_cleaned[loan_data_cleaned['loan_status'].str.contains('Late', na=False)].copy()

# Step 2: Calculate the percentage of customers at risk
total_customers = len(loan_data_cleaned)
at_risk_customers_count = len(at_risk_customers)
percentage_at_risk = (at_risk_customers_count / total_customers) * 100
print(f"Percentage of Customers Behind on Payments: {percentage_at_risk:.2f}%")

# Step 3: Calculate potential loss if these loans were to be Charged Off
# Calculate expected revenue for at-risk customers (term * installment)
at_risk_customers.loc[:, 'expected_revenue'] = at_risk_customers['term'].str.extract(r'(\d+)')[0].astype(int) * at_risk_customers['instalment']

# Calculate potential loss for at-risk customers (expected revenue - total payment so far)
at_risk_customers.loc[:, 'potential_loss'] = at_risk_customers['expected_revenue'] - at_risk_customers['total_payment']

# Summarize total potential loss if these customers defaulted
total_potential_loss = at_risk_customers['potential_loss'].sum()
print(f"Total Potential Loss if At-Risk Customers Default: ${total_potential_loss:,.2f}")

# Step 4: Calculate projected loss if they finish the full term
# For this step, the loss is the potential loss calculated above (if customers continue to default)
projected_loss_if_defaulted = total_potential_loss

# Step 5: Combine with already defaulted customers (Charged Off)
charged_off_customers = loan_data_cleaned[loan_data_cleaned['loan_status'] == 'Charged Off'].copy()
charged_off_customers.loc[:, 'expected_revenue'] = charged_off_customers['term'].str.extract(r'(\d+)')[0].astype(int) * charged_off_customers['instalment']
charged_off_customers.loc[:, 'loss'] = charged_off_customers['expected_revenue'] - charged_off_customers['total_payment']

total_charged_off_loss = charged_off_customers['loss'].sum()

# Step 6: Calculate combined loss and percentage of total expected revenue
total_combined_loss = total_charged_off_loss + total_potential_loss
total_expected_revenue = loan_data_cleaned['term'].str.extract(r'(\d+)')[0].astype(int).sum() * loan_data_cleaned['instalment'].mean()
percentage_combined_loss = (total_combined_loss / total_expected_revenue) * 100

print(f"Total Loss if At-Risk and Charged Off Customers Default: ${total_combined_loss:,.2f}")
print(f"Percentage of Total Expected Revenue: {percentage_combined_loss:.2f}%")

# Step 7: Save summary results to CSV
summary_data = pd.DataFrame({
    'Metric': ['Percentage of Customers Behind on Payments', 'Total Potential Loss if Default', 
               'Total Combined Loss (At-Risk + Charged Off)', 'Percentage of Total Expected Revenue'],
    'Value': [f"{percentage_at_risk:.2f}%", f"${total_potential_loss:,.2f}", 
              f"${total_combined_loss:,.2f}", f"{percentage_combined_loss:.2f}%"]
})

output_file = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/at_risk_customers_summary.csv'
summary_data.to_csv(output_file, index=False)
print(f"Summary of at-risk customers saved to: {output_file}")

# Optional: Visualize the combined loss
plt.figure(figsize=(10, 6))
plt.bar(['Charged Off Customers', 'At-Risk Customers'], [total_charged_off_loss, total_potential_loss], color=['salmon', 'orange'])
plt.title('Projected Loss from Charged Off and At-Risk Customers')
plt.ylabel('Projected Loss ($)')
plt.grid(True)

output_dir = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/03_Data_Analysis/visualisations/'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f'{output_dir}/combined_loss_projected.png')

plt.show()
