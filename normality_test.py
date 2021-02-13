# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 01:37:31 2021

@author: HP
"""

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from statsmodels.formula.api import ols
col_list = ["OrgSize","JobSeek","YearsCode"]
data = pd.read_csv("survey_results_public.csv",usecols=col_list)
#data = data.replace('NA', np.nan)
data.dropna()
#data.head
#list(data.columns.values)
print(data.shape)


data['OrgSize'].value_counts()
#data['Hobbyist'] = data[np.isfinite(data['Hobbyist'])]
data['OrgSize'] = data['OrgSize'].map({'Just me - I am a freelancer, sole proprietor, etc.': 1, '2 to 9 employees': 2,
                                          '20 to 99 employees': 3, '100 to 499 employees': 4,
                                    '500 to 999 employees': 5, '1,000 to 4,999 employees': 6})
data['JobSeek'].value_counts()
data['JobSeek'] = data['JobSeek'].map({'I am not interested in new job opportunities': 1, 'I\'m not actively looking, but I am open to new opportunities': 2,
                                    'I am actively looking for a job': 3})


data['YearsCode'].value_counts()
data['YearsCode'] = data['YearsCode'].map({'Less than 1 year': 1, 'More than 50 years': 2})

sns.distplot(data['OrgSize'])

qqplot(data['OrgSize'], line='s')
plt.show()


sns.distplot(data['JobSeek'])

qqplot(data['JobSeek'], line='s')
plt.show()

sns.distplot(data['YearsCode'])

qqplot(data['YearsCode'], line='s')
plt.show()


#checking equal variance with boxplot
boxplot = data.boxplot(column=['OrgSize', 'JobSeek', 'YearsCode'])

#checking equal variance with boxplot
boxplot = data.boxplot(column=['YearsCode'])
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
data_out = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]
data_out.shape
sns.boxplot(x=data_out['YearsCode'])

import seaborn as sns
sns.boxplot(x=data['YearsCode'])

sns.boxplot(x=data_out['YearsCode'])

