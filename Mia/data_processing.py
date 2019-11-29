#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

# Drop irrelavant columns 
drop_list = ['Unnamed: 0','id','member_id','funded_amnt','url','desc','title']

drop_for_grade_list = ['funded_amnt_inv','int_rate','installment','issue_d','loan_status','pymnt_plan','out_prncp','out_prncp_inv']

df_processed = df_processed.drop(drop_list, axis=1)
df_processed = df_processed.drop(drop_for_grade_list, axis=1)

# Convert categorical to numerical 
df_processed['term'] = df_processed['term'].apply(lambda x: int(x.split()[0]))
df_processed['emp_length'] = df_processed['emp_length'].str.extract('(\d+)') 
#10 means more than 10 years 

# Convert to Datetime
df_processed['earliest_cr_line'] = pd.to_datetime(df_processed['earliest_cr_line'])

# Missing Values 

df_processed.mths_since_last_record = df_processed.mths_since_last_record.fillna(0)
df_processed.mths_since_last_delinq = df_processed.mths_since_last_delinq.fillna(0)

df_processed.emp_title = df_processed.emp_title.fillna('None')
df_processed.emp_length = df_processed.emp_length.fillna(0)

df_processed.revol_util = df_processed.revol_util.fillna(0)

df_processed.dti = df_processed.dti.fillna(df_processed.revol_bal / df_processed.annual_inc)

