import pandas as pd

class DataFrameInfo:
    """
    A class to extract and display useful information about a DataFrame for EDA.
    """
    
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        """
        Describe all columns in the DataFrame, including their data types and basic information.
        """
        print("Column Descriptions:")
        print(self.df.info())
        print("\n")

    def extract_statistics(self):
        """
        Extract statistics (mean, median, standard deviation) from numeric columns.
        """
        print("Statistical Overview:")
        print(self.df.describe())
        print("\n")
        print("Median Values:")
        print(self.df.median(numeric_only=True))
        print("\nStandard Deviation:")
        print(self.df.std(numeric_only=True))
        print("\n")

    def count_distinct_values(self):
        """
        Count distinct values in all categorical columns.
        """
        print("Distinct Value Counts (Categorical Columns):")
        categorical_columns = self.df.select_dtypes(include=['category', 'object']).columns
        for col in categorical_columns:
            print(f"{col}: {self.df[col].nunique()} distinct values")
        print("\n")

    def print_shape(self):
        """
        Print the shape of the DataFrame.
        """
        print(f"Shape of DataFrame: {self.df.shape}")
        print("\n")

    def count_null_values(self):
        """
        Count the number and percentage of NULL values in each column.
        """
        print("NULL Value Counts and Percentages:")
        null_counts = self.df.isnull().sum()
        null_percentages = (self.df.isnull().mean() * 100).round(2)
        null_info = pd.DataFrame({'Null Count': null_counts, 'Percentage': null_percentages})
        print(null_info[null_info['Null Count'] > 0])
        print("\n")

# Example usage:
# Initialize the DataFrameInfo class with your transformed DataFrame
df_info = DataFrameInfo(loan_data_transformed)

# Use the methods to extract useful information for EDA
df_info.describe_columns()
df_info.extract_statistics()
df_info.count_distinct_values()
df_info.print_shape()
df_info.count_null_values()
