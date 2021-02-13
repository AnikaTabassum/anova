# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 01:37:31 2021

@author: ANIKA TABASSUM
"""
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
data = pd.read_csv("survey_results_public.csv")
data = data.replace('NA', np.nan)

#null hypothesis: non-experienced programmer who works in very large organization, are not interested to switch job

# getting dataframe with very large org size
organization_size_very_large=data[data['OrgSize'].str.contains('1,000 to 4,999 employees', na=False)]

#people who are interested in job change and works in a very large organization
job_interested_very=organization_size_very_large['JobSeek'].str.contains('I am actively looking for a job', na=False)

#yearscode of people who are interested in job change and works in a very large organization
very_large_interested=organization_size_very_large[job_interested_very]['YearsCode']
very_large_interested=very_large_interested.dropna()
very_large_interested=very_large_interested.replace('Less than 1 year',0.5)
very_large_interested=very_large_interested.replace('More than 50 years',55)
very_large_interested=pd.to_numeric(very_large_interested)
very_large_interested=very_large_interested[very_large_interested>0]
print(very_large_interested)


# getting dataframe with very large org size
organization_size_very_large=data[data['OrgSize'].str.contains('1,000 to 4,999 employees', na=False)]

#people who are interested in job change and works in a very large organization
job_not_interested_very=organization_size_very_large['JobSeek'].str.contains('I am not interested in new job opportunities', na=False)

#people who are interested in job change and works in a very large organization
very_large_not_interested=organization_size_very_large[job_not_interested_very]['YearsCode']
very_large_not_interested=very_large_not_interested.dropna()
very_large_not_interested=very_large_not_interested.replace('Less than 1 year',0.5)
very_large_not_interested=very_large_not_interested.replace('More than 50 years',55)
very_large_not_interested=pd.to_numeric(very_large_not_interested)
very_large_not_interested=very_large_not_interested[very_large_not_interested>0]
print(very_large_not_interested)

# very_large_interested.plot.box()
# very_large_not_interested.plot.box()
print(sm.qqplot(np.log(very_large_interested), line = 'r'))
#### better result after log transformation
print(sm.qqplot(very_large_not_interested, line = 'r'))


t,p = stats.ttest_ind(very_large_interested,very_large_not_interested,equal_var=True)
print("before","t = %g p = %g" % (t,p))

print(very_large_interested.describe())
print("median",very_large_interested.median())
print("mode",very_large_interested.mode())


print(very_large_not_interested.describe())
print("median--2",very_large_not_interested.median())
print("mode---2",very_large_not_interested.mode())

result=stats.levene(very_large_interested,very_large_not_interested)
print(result)


anova_result = stats.f_oneway(very_large_interested,very_large_not_interested)
print(anova_result)
#output
# F_onewayResult(statistic=29.940415902841828, pvalue=5.0659762818620844e-08)

t_result_t, t_result_p = stats.ttest_ind(very_large_interested, very_large_not_interested, equal_var=True)
print("t = %g p = %g" % (t_result_t,t_result_p))

l=very_large_interested.quantile(.25)
u= very_large_interested.quantile(.75)
IQR=u-l
upper_limit= u+1.5*IQR
lower_limit= l-1.5*IQR
very_large_interested_new=very_large_interested[(very_large_interested<=upper_limit) & (very_large_interested>=lower_limit)]
very_large_interested_new.plot.box()
sm.qqplot(very_large_interested_new, line = 's')


n_l=very_large_not_interested.quantile(.25)
n_u= very_large_not_interested.quantile(.75)
n_IQR=n_u-n_l
upper_limit_n= n_u+1.5*n_IQR
lower_limit_n= n_l-1.5*n_IQR
very_large_not_interested_new=very_large_not_interested[(very_large_not_interested<=upper_limit_n) & (very_large_not_interested>=lower_limit_n)]
very_large_not_interested_new.plot.box()
sm.qqplot((very_large_not_interested_new), line = 's')


print(very_large_interested_new.describe())
print("median_new",very_large_interested_new.median())
print("mode_new",very_large_interested_new.mode())


print(very_large_not_interested_new.describe())
print("median--2_new",very_large_not_interested_new.median())
print("mode---2_new",very_large_not_interested_new.mode())


anova_result2 = stats.f_oneway(very_large_interested_new,very_large_not_interested_new)
print(anova_result2)
#F_onewayResult(statistic=64.11284005171912, pvalue=2.1007042178505517e-15)

t_result_t, t_result_p = stats.ttest_ind(very_large_interested_new, very_large_not_interested_new, equal_var=True)
print("t = %g p = %g" % (t_result_t,t_result_p))


#aonva gives result with high statistics and very low p value 
#  we can reject the null hypothesis of equal averages
