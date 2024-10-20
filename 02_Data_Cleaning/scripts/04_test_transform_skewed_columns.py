import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class DataFrameTransform:
    def __init__(self, df):
        """
        Initialize the DataFrameTransform class with a DataFrame.
        """
        self.df = df
    
    def identify_skewed_columns(self, threshold=1, exclude_columns=None):
        """
        Identify skewed columns in the DataFrame based on the given skewness threshold.
        
        Parameters:
        threshold (float): The skewness threshold to consider a column as skewed. Default is 1.
        exclude_columns (list): List of columns to exclude from skewness check.
        
        Returns:
        List of skewed columns.
        """
        if exclude_columns is None:
            exclude_columns = []
        
        skewness = self.df.drop(columns=exclude_columns).skew(numeric_only=True)
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        print(f"Skewed columns (threshold={threshold}): {skewed_columns}")
        return skewed_columns

    def transform_column(self, column, method):
        """
        Apply a transformation to reduce skewness for the specified column.
        
        Parameters:
        column (str): The column to transform.
        method (str): The transformation method ('log', 'sqrt', or 'boxcox').
        
        Returns:
        Transformed column as a Pandas Series.
        """
        if method == 'log':
            return np.log1p(self.df[column])  # log(x + 1) to avoid log(0)
        elif method == 'sqrt':
            return np.sqrt(self.df[column])
        elif method == 'boxcox':
            # Box-Cox requires positive values, so we add 1 to all values if necessary
            transformed_data, _ = stats.boxcox(self.df[column] + 1)
            return pd.Series(transformed_data, index=self.df.index)
    
    def test_transformations(self, column):
        """
        Test log, sqrt, and boxcox transformations on a skewed column.
        Returns the transformation method that best reduces skewness.
        """
        original_skew = self.df[column].skew()
        transformations = {'log': None, 'sqrt': None, 'boxcox': None}
        skews = {}

        # Apply transformations and calculate skewness
        for method in transformations.keys():
            transformed_column = self.transform_column(column, method)
            skews[method] = transformed_column.skew()

        # Find the method that reduces skewness the most
        best_method = min(skews, key=lambda k: abs(skews[k]))
        print(f"Best transformation for {column}: {best_method} (Original Skew: {original_skew:.2f}, {best_method} Skew: {skews[best_method]:.2f})")
        return best_method

# Load the cleaned dataset
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_milestone_4_ready.csv'
loan_data_cleaned = pd.read_csv(file_path)

# Step 1: Identify skewed columns, excluding 'id' and 'member_id'
df_transformer = DataFrameTransform(loan_data_cleaned)
exclude_columns = ['id', 'member_id']  # Exclude key columns
skewed_columns = df_transformer.identify_skewed_columns(threshold=1, exclude_columns=exclude_columns)

# Step 2: Test transformations and choose the best method for each column
for col in skewed_columns:
    best_method = df_transformer.test_transformations(col)

# After identifying the best transformations, we will apply them in the next step.
