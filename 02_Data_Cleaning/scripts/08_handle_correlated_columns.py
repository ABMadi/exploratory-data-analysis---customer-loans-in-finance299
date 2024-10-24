import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    def __init__(self, df):
        """
        Initialize the Plotter class with a DataFrame.
        """
        self.df = df

    def plot_correlation_matrix(self, save_path=None):
        """
        Compute and plot the correlation matrix for the dataset.
        
        Parameters:
        save_path (str): File path to save the plot (optional).
        """
        # Select only numeric columns, including 'total_rec_prncp' and 'instalment' for analysis
        numeric_df = self.df.drop(columns=['id', 'member_id']).select_dtypes(include=[np.number])
        
        plt.figure(figsize=(12, 8))
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Matrix")
        
        if save_path:
            plt.savefig(save_path)
            print(f"Correlation matrix plot saved to {save_path}")
        else:
            plt.show()

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def identify_highly_correlated_columns(self, threshold=0.8, exclude_from_removal=None):
        """
        Identify columns that are highly correlated with each other, but prevent specific columns from being removed.
        
        Parameters:
        threshold (float): Correlation threshold for identifying highly correlated columns. Default is 0.8.
        exclude_from_removal (list): List of columns that should not be removed, even if they are highly correlated.
        
        Returns:
        List of columns to remove based on high correlation.
        """
        if exclude_from_removal is None:
            exclude_from_removal = ['total_rec_prncp', 'instalment']  # Columns that shouldn't be dropped

        # Select only numeric columns
        numeric_df = self.df.drop(columns=['id', 'member_id']).select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr().abs()  # Get absolute correlation values
        upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))

        # Identify columns to remove, excluding the specified columns
        to_remove = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold) and column not in exclude_from_removal]
        print(f"Columns to remove based on correlation threshold {threshold}: {to_remove}")
        return to_remove

    def remove_correlated_columns(self, columns):
        """
        Remove the specified columns from the DataFrame.
        
        Parameters:
        columns (list): List of columns to remove.
        
        Returns:
        DataFrame with specified columns removed.
        """
        self.df.drop(columns=columns, inplace=True)
        return self.df

# Load the dataset after outliers have been handled
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v4_outliers_handled.csv'
loan_data_no_outliers = pd.read_csv(file_path)

# Step 1: Compute and visualise the correlation matrix (including 'total_rec_prncp' and 'instalment')
plotter = Plotter(loan_data_no_outliers)
correlation_matrix_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/02_Data_Cleaning/visualisations/correlation_matrix.png'
plotter.plot_correlation_matrix(save_path=correlation_matrix_save_path)

# Step 2: Identify highly correlated columns (using 0.8 as the threshold), excluding 'total_rec_prncp' and 'instalment' from removal
df_transformer = DataFrameTransform(loan_data_no_outliers)
correlated_columns = df_transformer.identify_highly_correlated_columns(threshold=0.8)

# Step 3 & 4: Remove the highly correlated columns and save the updated dataset
loan_data_final = df_transformer.remove_correlated_columns(correlated_columns)

# Step 4: Save the final dataset without highly correlated columns (but keeping 'total_rec_prncp' and 'instalment')
final_data_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v5_with_instalment_and_total_rec_prncp.csv'
loan_data_final.to_csv(final_data_save_path, index=False)
print(f"Final dataset saved to: {final_data_save_path}")
