# Loan Portfolio EDA and Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [Data Cleaning Steps](#data-cleaning-steps)
- [Analysis Steps](#analysis-steps)
- [License](#license)

## Project Overview
This project focuses on conducting an exploratory data analysis (EDA) of a loan portfolio dataset. The goal is to help a financial institution make more informed decisions regarding loan approvals, risk management, and profitability. The analysis includes various data cleaning steps to prepare the data for meaningful insights.

### Aim of the Project:
- Clean the loan portfolio data to ensure accurate and reliable analysis.
- Explore relationships and patterns within the data.
- Analyze risk factors for loan defaults.
- Visualize key indicators to aid in risk management decisions.

### What I Learned:
- How to handle missing data and ensure data quality.
- How to identify and remove outliers to improve data accuracy.
- Techniques for reducing skewness and handling highly correlated columns to prevent multicollinearity.
- How to identify key indicators of loan default risk using EDA and visualizations.

## Installation Instructions
To set up this project on your local machine, follow these steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ABMadi/exploratory-data-analysis---customer-loans-in-finance299.git
2. **Navigate to the project directory**:
   ```bash
   cd exploratory-data-analysis---customer-loans-in-finance299

3. **Install required dependencies**: You'll need Python and the following libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scipy

You can install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
## Usage Instructions

1. Ensure that your environment is set up with the necessary dependencies.

2. **Data Cleaning**: Run the Python scripts in the **02_Data_Cleaning/scripts/** folder sequentially to process the data. Each script corresponds to a specific data cleaning step, such as handling null values, outliers, and correlated columns.

3. **Analysis**: Run the scripts in the **03_Data_Analysis/scripts/** folder to perform the analyses. These scripts include:

- Loan payment summary.
- Calculating the projected loss from - charged-off loans.
- Visualizing potential default indicators.
4. The final cleaned dataset and analysis visualizations will be saved in the 01_Results/ folder.

## File Structure
Finance_Project/
├── 01_Results/
│   ├── Comparison_Results/
│   │   ├── home_ownership_comparison.png
│   │   ├── loan_grades_comparison.png
│   │   ├── dti_comparison.png
│   │   ├── out_prncp_comparison.png
│   │   ├── total_payment_comparison.png
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
├── 03_Data_Analysis/
│   ├── scripts/
│   │   ├── 01_loan_payment_summary.py
│   │   ├── 02_calculate_charged_off_loans.py
│   │   ├── 03_calculate_projected_loss.py
│   │   ├── 04_analyze_at_risk_customers.py
│   │   ├── 05_analyze_default_indicators.py
│   │   ├── 06_visualize_default_indicators.py
│   ├── visualisations/

## Data Cleaning Steps
1. **Corrected Formats**: Converted columns to appropriate data types and ensured dates and numerical values were in the correct format.

2. **Handled Missing Values**: Imputed missing values using median and mode imputation techniques.

3. **Reduced Skewness**: Applied Box-Cox transformations to skewed columns to normalise data distributions.

4. **Removed Outliers**: Identified and removed or capped extreme outliers using the IQR method.

5. **Handled Correlated Columns**: Identified highly correlated columns and removed the redundant ones to reduce multicollinearity.

## Analysis Steps
1. **Loan Payment Summary**: A summary of the loan payments, including the total amount recovered and projected revenue over 6 months.

2. **Charged-Off Loan Analysis**: Calculated the percentage of charged-off loans and the potential loss incurred due to these loans.

3. **At-Risk Customer Analysis**: Identified customers at risk of default and calculated the potential loss if these customers were to default.

4. **Default Indicator Visualization**: Visualized key indicators (such as loan grades, DTI, and home ownership) to highlight trends among charged-off and at-risk customers.

## License
This project is licensed under the MIT License.