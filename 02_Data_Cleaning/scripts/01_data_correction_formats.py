import pandas as pd

class DataTransform:
    """
    A class to handle data transformations for the loan dataset.
    """
    
    def __init__(self, df):
        self.df = df

    def convert_to_datetime(self, columns):
        """
        Convert specified columns to datetime format.
        
        Parameters:
        columns (list): List of column names to convert.
        
        Returns:
        DataFrame: Updated DataFrame with converted datetime columns.
        """
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], format='%b-%Y', errors='coerce')
        return self.df
    
    def convert_to_categorical(self, columns):
        """
        Convert specified columns to categorical type.
        
        Parameters:
        columns (list): List of column names to convert.
        
        Returns:
        DataFrame: Updated DataFrame with categorical columns.
        """
        for col in columns:
            self.df[col] = self.df[col].astype('category')
        return self.df

    def transform_employment_length(self):
        """
        Clean and convert the employment_length column to numeric values.
        
        Returns:
        DataFrame: Updated DataFrame with numeric employment length.
        """
        self.df['employment_length'] = self.df['employment_length'].replace({
            '10+ years': 10,
            '< 1 year': 0,
            '1 year': 1,
            '2 years': 2,
            '3 years': 3,
            '4 years': 4,
            '5 years': 5,
            '6 years': 6,
            '7 years': 7,
            '8 years': 8,
            '9 years': 9
        }).astype(float)
        return self.df

# Load the raw dataset
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/raw/loan_payments_data.csv'
loan_data = pd.read_csv(file_path)

# Initialize the DataTransform class with the loaded dataset
data_transformer = DataTransform(loan_data)

# Step 1: Convert date columns to datetime format
date_columns = ['issue_date', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
loan_data_transformed = data_transformer.convert_to_datetime(date_columns)

# Step 2: Convert certain columns to categorical
categorical_columns = ['loan_status', 'grade', 'sub_grade', 'home_ownership', 'verification_status']
loan_data_transformed = data_transformer.convert_to_categorical(categorical_columns)

# Step 3: Transform the employment_length column
loan_data_transformed = data_transformer.transform_employment_length()

# Save the transformed dataset with a new versioned name
save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v1_corrected_formats.csv'
loan_data_transformed.to_csv(save_path, index=False)

print(f"Transformed data saved to {save_path}")
