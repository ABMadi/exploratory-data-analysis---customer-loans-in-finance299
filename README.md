#!/bin/bash

# Loan Portfolio EDA and Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [Data Cleaning Steps](#data-cleaning-steps)
- [Data Analysis Steps](#data-analysis-steps)
- [License](#license)

## Project Overview
This project focuses on conducting an exploratory data analysis (EDA) of a loan portfolio dataset. 
The goal is to help a financial institution make more informed decisions regarding loan approvals, 
risk management, and profitability. The analysis includes various data cleaning steps to prepare 
the data for meaningful insights, followed by data analysis to summarize key insights.

### Aim of the Project:
- Clean the loan portfolio data to ensure accurate and reliable analysis.
- Explore relationships and patterns within the data.
- Generate insights regarding loan payments, recoveries, and charged-off loans.
- Build a foundation for further analysis and model-building.

### What I Learned:
- How to handle missing data and ensure data quality.
- How to identify and remove outliers to improve data accuracy.
- Techniques for reducing skewness and handling highly correlated columns to prevent multicollinearity.
- How to perform key analysis, such as calculating loan recoveries, payments, and identifying losses from charged-off loans.

## Installation Instructions
To set up this project on your local machine, follow these steps:

1. Clone the repository:
   git clone https://github.com/ABMadi/exploratory-data-analysis---customer-loans-in-finance299.git

2. Navigate to the project directory:
   cd exploratory-data-analysis---customer-loans-in-finance299

3. Install required dependencies: You'll need Python and the following libraries
   - pandas
   - numpy
   - matplotlib
   - seaborn
   - scipy

   You can install the dependencies using:
   pip install -r requirements.txt

## Usage Instructions
1. Ensure that your environment is set up with the necessary dependencies.

2. Run the Python scripts in the 02_Data_Cleaning/scripts/ folder sequentially to process and clean the data.
   Each script corresponds to a specific data cleaning step, such as handling null values, outliers, and correlated columns.

3. The final cleaned dataset will be saved in the data/processed/ folder.

4. Once the data is cleaned, move on to the scripts in the 03_Data_Analysis/scripts/ folder to conduct analysis on the cleaned dataset.
   The analysis includes summarizing loan recoveries and identifying losses from charged-off loans.

## File Structure
Finance_Project/
│
├── 02_Data_Cleaning/
│   ├── scripts/
│   │   ├── 01_data_correction_formats.py
│   │   ├── 02_null_value_transformation.py
│   │   ├── 03_identifying_visualising_skewed_columns.py
│   │   ├── 04_test_transform_skewed_columns.py
│   │   ├── 05_apply_transform_skewed_columns.py
│   │   ├── 06_handle_outliers.py
│   │   ├── 07_revisualise_after_outliers.py
│   │   ├── 08_handle_correlated_columns.py
│   ├── visualisations/
│   │   ├── null_values_before_cleaning.png
│   │   ├── skewed_columns_before.png
│   │   ├── skewed_columns_after.png
│   │   ├── outliers_boxplots_before.png
│   │   ├── outliers_boxplots_after.png
│   │   ├── correlation_matrix.png
│   ├── processed/
│   │   ├── loan_payments_data_v1_formats_corrected.csv
│   │   ├── loan_payments_data_v2_null_imputation.csv
│   │   ├── loan_payments_data_v3_skewness_corrected.csv
│   │   ├── loan_payments_data_v4_outliers_handled.csv
│   │   ├── loan_payments_data_v5_correlated_columns_removed.csv
│
├── 03_Data_Analysis/
│   ├── scripts/
│   │   ├── 01_loan_payment_summary.py
│   │   ├── 02_calculate_charged_off_loans.py
│   ├── visualisations/
│   │   ├── percentage_recovered.png
│   │   ├── payments_in_6_months.png
│   ├── processed/
│   │   ├── loan_payments_data_summary.csv
│   │   ├── charged_off_summary.csv
│
└── README.md

## Data Cleaning Steps
1. Corrected Formats: Converted columns to appropriate data types and ensured dates and numerical values were in the correct format.

2. Handled Missing Values: Imputed missing values using median and mode imputation techniques.

3. Reduced Skewness: Applied Box-Cox transformations to skewed columns to normalise data distributions.

4. Removed Outliers: Identified and removed or capped extreme outliers using the IQR method.

5. Handled Correlated Columns: Identified highly correlated columns and removed the redundant ones to reduce multicollinearity.

## Data Analysis Steps
1. Loan Payment Summary: Summarized the percentage of loans recovered and calculated the total amount expected to be paid in the next 6 months, including interest. 
   The results are saved and visualized in the `03_Data_Analysis/visualisations/` folder.

2. Charged Off Loans: Identified loans that were "Charged Off" in the dataset, calculated the percentage of charged-off loans, and determined the total amount paid before they were charged off. 
   The results are saved and visualized, and the summary can be found in the `03_Data_Analysis/processed/charged_off_summary.csv` file.

## License
This project is licensed under the MIT License.
