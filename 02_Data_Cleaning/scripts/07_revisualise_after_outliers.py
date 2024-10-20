import pandas as pd
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

# Load the dataset after outliers have been handled
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v4_outliers_handled.csv'
loan_data_no_outliers = pd.read_csv(file_path)

# List of columns to visualise
columns_to_check = ['annual_inc', 'delinq_2yrs', 'inq_last_6mths', 'open_accounts', 'out_prncp', 
                    'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 
                    'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 
                    'last_payment_amount', 'collections_12_mths_ex_med']

# Step 3: Re-visualise the data after handling outliers
plotter = Plotter(loan_data_no_outliers)
boxplot_save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/02_Data_Cleaning/visualisations/outliers_boxplots_after.png'
plotter.plot_boxplots(columns_to_check, save_path=boxplot_save_path)
