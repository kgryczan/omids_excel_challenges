import pandas as pd
import numpy as np

path = 'CH-099 Random Selection Part 2.xlsx'
input = pd.read_excel(path, usecols='B:C', skiprows=1)

def sample_dept_and_emp(input_df, n):
    n = 4
    n_distinct = len(input_df['Department'].unique())
    emp_per_dept = input_df['Department'].value_counts().reset_index()

    while True:
        samp_depts = np.random.choice(input_df['Department'].unique(), n, replace=True, p=np.repeat(1/n_distinct, n_distinct))
        samp_depts = pd.DataFrame({'Department': samp_depts})
        samp_depts['nr'] = samp_depts.groupby('Department').cumcount() + 1
        check = pd.merge(samp_depts, emp_per_dept, left_on='Department', right_on='Department', how='left')

        if (check['count'] >= check['nr']).all():
            break

    samp_empl = pd.merge(input_df, samp_depts, on='Department', how='left').dropna()
    samp_empl = samp_empl.groupby('Department').apply(lambda x: x[x['nr'] == x['nr'].max()]).reset_index(drop=True)
    samp_empl["nr"] = samp_empl["nr"].astype(int)
    samp_empl = samp_empl.groupby('Department').apply(lambda x: x.sample(x['nr'].max())).reset_index(drop=True)
    samp_empl = samp_empl.drop(columns='nr')

    return samp_empl

samp_empl = sample_dept_and_emp(input, 4)
print(samp_empl)

#    Department Staff ID
# 0  Production     S_16
# 1  Production     S_05
# 2  Production     S_17
# 3  Production     S_18

#    Department Staff ID
# 0          IT     S_09
# 1   Marketing     S_03
# 2   Marketing     S_02
# 3  Production     S_05