# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here
categorical_var = bank.select_dtypes(include='object')
numerical_var = bank.select_dtypes(include='number')

banks = bank.drop(columns='Loan_ID')
banks.isnull().sum()
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)

avg_loan_amount = pd.pivot_table(banks,
                                 index=['Gender', 'Married', 'Self_Employed'],
                                 values='LoanAmount',
                                 aggfunc='mean')
avg_loan_amount

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes')
                         & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No')
                          & (banks['Loan_Status'] == 'Y')]
percentage_se = len(loan_approved_se) * 100 / len(banks)
percentage_nse = len(loan_approved_nse) * 100 / len(banks)

big_loan_term = len(
    banks[banks['Loan_Amount_Term'].apply(lambda x: x / 12) >= 25])

loan_groupby = banks.groupby(by='Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()


