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

    def plot_boxplots(self, columns, save_path=None):
        """
        Plot boxplots for the specified columns to visualise outliers.
        
        Parameters:
        columns (list): List of columns to plot.
        save_path (str): File path to save the plot (optional).
        """
        num_cols = len(columns)
        plt.figure(figsize=(15, 5 * num_cols))
        
        for i, col in enumerate(columns, 1):
            plt.subplot(num_cols, 1, i)
            sns.boxplot(x=self.df[col])
            plt.title(f"Boxplot of {col}")
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            print(f"Plot saved to {save_path}")
        else:
            plt.show()

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def remove_outliers_iqr(self, columns):
        """
        Remove outliers from specified columns using the IQR method.
        
        Parameters:
        columns (list): List of columns to remove outliers from.
        
        Returns:
        DataFrame with outliers removed.
        """
        for col in columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Remove rows with outliers
            self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
        
        return self.df

    def cap_outliers_iqr(self, columns):
        """
        Cap outliers from specified columns using the IQR method.
        Values above or below the bounds will be capped.
        
        Parameters:
        columns (list): List of columns to cap outliers from.
        
        Returns:
        DataFrame with outliers capped.
        """
        for col in columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Cap outliers at the lower and upper bounds
            self.df[col] = np.where(self.df[col] < lower_bound, lower_bound, self.df[col])
            self.df[col] = np.where(self.df[col] > upper_bound, upper_bound, self.df[col])
        
        return self.df

# Load the cleaned dataset (after skewness correction)
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v3_skewness_corrected.csv'
loan_data_cleaned = pd.read_csv(file_path)

# List of columns to check for outliers
columns_to_check = ['annual_inc', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'out_prncp', 
                    'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 
                    'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 
                    'last_payment_amount', 'collections_12_mths_ex_med']

# Step 2: Remove or Cap the outliers using IQR method
df_transformer = DataFrameTransform(loan_data_cleaned)

# Option 1: Remove outliers
loan_data_no_outliers = df_transformer.remove_outliers_iqr(columns_to_check)

# Option 2: Cap outliers (uncomment this if you'd rather cap than remove)
# loan_data_no_outliers = df_transformer.cap_outliers_iqr(columns_to_check)

# Step 2: Save the dataset with outliers handled
transformed_data_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v4_outliers_handled.csv'
loan_data_no_outliers.to_csv(transformed_data_save_path, index=False)
print(f"Dataset with outliers handled saved to: {transformed_data_save_path}")
