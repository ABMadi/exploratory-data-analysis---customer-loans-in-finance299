# File: 02_Data_Cleaning/scripts/download_data.py

from db_utils import RDSDatabaseConnector, load_db_credentials

# Step 1: Load the database credentials
credentials = load_db_credentials('C:/Users/user/Documents/AiCore/Projects/Finance_Project/credentials.yaml')

# Step 2: Initialize the RDSDatabaseConnector with the credentials
db_connector = RDSDatabaseConnector(credentials)

# Step 3: Extract data from the 'loan_payments' table
loan_data_df = db_connector.extract_data_as_dataframe('loan_payments')

# Step 4: Save the extracted data to a .csv file
csv_file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/raw/loan_payments_data.csv'
db_connector.save_data_to_csv(loan_data_df, csv_file_path)
