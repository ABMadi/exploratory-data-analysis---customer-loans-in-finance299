import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Step 1: Identify skewed columns, excluding 'id' and 'member_id'
df_transformer = DataFrameTransform(loan_data_cleaned)
exclude_columns = ['id', 'member_id']  # Exclude key columns
skewed_columns = df_transformer.identify_skewed_columns(threshold=1, exclude_columns=exclude_columns)

# Step 2: Visualise the skewed columns
plotter = Plotter(loan_data_cleaned)
plot_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/02_Data_Cleaning/visualisations/skewed_columns_before.png'
plotter.plot_distribution(skewed_columns, save_path=plot_save_path)
