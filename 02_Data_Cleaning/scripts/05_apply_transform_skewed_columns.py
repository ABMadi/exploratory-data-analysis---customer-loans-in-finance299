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
    
    def apply_boxcox(self, column):
        """
        Apply Box-Cox transformation to the specified column.
        Adjust for any zero or negative values by adding 1.
        
        Parameters:
        column (str): The column to apply the transformation to.
        
        Returns:
        Transformed column as a Pandas Series.
        """
        transformed_data, _ = stats.boxcox(self.df[column] + 1)
        return pd.Series(transformed_data, index=self.df.index)

class Plotter:
    def __init__(self, df):
        """
        Initialize the Plotter class with a DataFrame.
        """
        self.df = df
    
    def plot_distribution(self, columns, save_path=None):
        """
        Plot the distribution of the specified columns to visualise skewness.
        
        Parameters:
        columns (list): List of columns to plot.
        save_path (str): File path to save the plot (optional).
        """
        num_cols = len(columns)
        plt.figure(figsize=(15, 5 * num_cols))
        
        for i, col in enumerate(columns, 1):
            plt.subplot(num_cols, 1, i)
            sns.histplot(self.df[col], kde=True)
            plt.title(f"Distribution of {col} (Skewness: {self.df[col].skew():.2f})")
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            print(f"Plot saved to {save_path}")
        else:
            plt.show()

# Load the cleaned dataset
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_milestone_4_ready.csv'
loan_data_cleaned = pd.read_csv(file_path)

# List of skewed columns based on the previous analysis
skewed_columns = ['annual_inc', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'out_prncp', 
                  'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 
                  'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 
                  'last_payment_amount', 'collections_12_mths_ex_med']

# Step 1: Apply Box-Cox transformation to all skewed columns
df_transformer = DataFrameTransform(loan_data_cleaned)
for col in skewed_columns:
    loan_data_cleaned[col] = df_transformer.apply_boxcox(col)

# Step 2: Save the transformed dataset
transformed_data_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v3_skewness_corrected.csv'
loan_data_cleaned.to_csv(transformed_data_save_path, index=False)
print(f"Transformed dataset saved to: {transformed_data_save_path}")

# Step 3: Visualise the distributions of the transformed columns
plotter = Plotter(loan_data_cleaned)
plot_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/02_Data_Cleaning/visualisations/skewed_columns_after.png'
plotter.plot_distribution(skewed_columns, save_path=plot_save_path)
