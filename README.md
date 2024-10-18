# Loan Portfolio EDA and Analysis

## Project Overview
This project is focused on performing exploratory data analysis (EDA) and subsequent analysis on a loan portfolio dataset for a financial institution. The aim is to gain insights into loan approval, risk management, and profitability by understanding patterns, relationships, and anomalies in the data.

## Folder Structure
The project is organised as follows:

- **data/**
  - `raw/`: Contains the original dataset in its raw form.
  - `processed/`: Contains cleaned datasets ready for analysis.
  
- **02_Data_Cleaning/scripts/**
  - Contains Python scripts used for data transformation and cleaning tasks.
  
- **02_Data_Cleaning/visualisations/**
  - Contains plots and visualisations generated during the EDA and data cleaning stages.

## Data Preparation

### NULL Value Handling
During data preparation, the following steps were taken to handle missing values:
- Columns with more than **50% missing values** were dropped.
- **Numeric columns**: Missing values were imputed using the **median**.
- **Categorical columns**: Missing values were imputed using the **mode**.

The following datasets were generated as part of this process:
- `loan_payments_data_v2_null_imputation.csv`: This file contains the cleaned dataset after handling missing values.
- `loan_payments_data_milestone_4_ready.csv`: A cleaned version of the dataset, ready for further analysis in Milestone 4.

### Visualisations
We generated visualisations to understand the distribution of NULL values:
- `null_values_before_cleaning.png`: Displays the NULL values in the dataset before any cleaning or imputation.
- `null_values_after_cleaning.png`: Displays the remaining NULL values (if any) after cleaning and imputation.

## Next Steps
The next milestone will involve performing more in-depth EDA tasks and analysis on the cleaned dataset. We will focus on deriving insights from the loan data, which can assist in making better loan approval decisions and risk management.
