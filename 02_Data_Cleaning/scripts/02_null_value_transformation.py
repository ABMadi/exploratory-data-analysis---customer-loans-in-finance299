import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    """
    A class to generate plots and visualise insights from the data.
    """
    
    def __init__(self, df):
        self.df = df

    def plot_null_values(self, save_path=None):
        """
        Plot a bar chart showing the count of NULL values for each column.
        If save_path is provided, the plot will be saved to the specified location.
        
        Parameters:
        save_path (str): The file path where the plot will be saved (optional).
        """
        null_counts = self.df.isnull().sum()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=null_counts.index, y=null_counts.values)
        plt.xticks(rotation=90)
        plt.title("NULL Values in Each Column")
        plt.ylabel("Number of NULLs")
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')  # Save the plot
            print(f"Plot saved to {save_path}")
        else:
            plt.show()  # Show the plot

class DataFrameTransform:
    """
    A class to perform transformations on the DataFrame, including handling missing values.
    """
    
    def __init__(self, df):
        self.df = df

    def check_nulls(self):
        """
        Check the number and percentage of NULL values in each column.
        """
        null_counts = self.df.isnull().sum()
        null_percentages = (self.df.isnull().mean() * 100).round(2)
        null_info = pd.DataFrame({'Null Count': null_counts, 'Percentage': null_percentages})
        return null_info[null_info['Null Count'] > 0]

    def drop_columns_with_nulls(self, threshold=50):
        """
        Drop columns with more than a specified percentage of NULL values.
        
        Parameters:
        threshold (int): The percentage threshold above which columns should be dropped.
        
        Returns:
        DataFrame: Updated DataFrame with columns dropped.
        """
        null_percentages = self.df.isnull().mean() * 100
        cols_to_drop = null_percentages[null_percentages > threshold].index
        self.df.drop(columns=cols_to_drop, inplace=True)
        return self.df

    def impute_missing_values(self):
        """
        Impute missing values in the DataFrame using mean or median, depending on the column type.
        - Mean for continuous variables (float).
        - Median for skewed distributions or where it is more appropriate.
        """
        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                if self.df[col].dtype in ['float64', 'int64']:
                    # Direct assignment to avoid inplace warning
                    self.df[col] = self.df[col].fillna(self.df[col].median())
                elif self.df[col].dtype == 'object':
                    # Direct assignment for categorical variables
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
        return self.df

    def save_transformed_data(self, save_path):
        """
        Save the transformed DataFrame to a CSV file.
        
        Parameters:
        save_path (str): The file path where the CSV will be saved.
        """
        self.df.to_csv(save_path, index=False)
        print(f"Transformed data saved to {save_path}")

# Load the dataset (assuming the transformed dataset is stored in a CSV file)
file_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v1_corrected_formats.csv'
loan_data_transformed = pd.read_csv(file_path)

# Step 1: Initialize the DataFrameTransform class with the transformed DataFrame
df_transformer = DataFrameTransform(loan_data_transformed)

# Step 2: Check for NULL values before cleaning and save the plot
null_info_before = df_transformer.check_nulls()
print("NULL values before dropping columns:\n", null_info_before)

# Plot the NULL values before cleaning
plotter = Plotter(loan_data_transformed)
plot_save_path_before = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/02_Data_Cleaning/visualisations/null_values_before_cleaning.png'
plotter.plot_null_values(save_path=plot_save_path_before)

# Step 3: Drop columns with more than 50% NULL values
loan_data_cleaned = df_transformer.drop_columns_with_nulls(threshold=50)

# Step 4: Impute remaining missing values with median or mean
loan_data_cleaned = df_transformer.impute_missing_values()

# Step 5: Check for NULL values again after cleaning and save the plot
null_info_after = df_transformer.check_nulls()
print("NULL values after imputation:\n", null_info_after)

# Plot the NULL values after cleaning (should show zero NULLs)
plot_save_path_after = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/02_Data_Cleaning/visualisations/null_values_after_cleaning.png'
plotter = Plotter(loan_data_cleaned)
plotter.plot_null_values(save_path=plot_save_path_after)

# Step 6: Save the cleaned and imputed data with a versioned filename
save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v2_null_imputation.csv'
df_transformer.save_transformed_data(save_path)

# Step 6: Save the cleaned and imputed data with a versioned filename
save_path = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_v2_null_imputation.csv'
df_transformer.save_transformed_data(save_path)

# Save a separate copy of the cleaned DataFrame for Milestone 4 analysis
save_path_milestone_4 = 'C:/Users/user/Documents/AiCore/Projects/Finance_Project/data/processed/loan_payments_data_milestone_4_ready.csv'
loan_data_cleaned.to_csv(save_path_milestone_4, index=False)

print(f"Cleaned DataFrame saved for Milestone 4 analysis at: {save_path_milestone_4}")
