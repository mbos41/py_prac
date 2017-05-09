
# coding: utf-8

# # Michael Bostwick
# ### Data Science Internship Work Sample
# 
# ### Q1.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('intern2017.csv', header = 0)
df.head(5)
df.status.unique()

df['success'] = (df.status == 'succeeded')

# A.
print(df.groupby(['gateway', 'transaction_type'])['success'].mean())

df['date'] = pd.to_datetime(df.epoch_date, unit='s')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['month_year'] = (df.year - 2014)*12 + df.month
df_a = df[(df['gateway'] == 'GA') & (df['transaction_type'] == 'Purchase') & (df['year'] > 2013)]
df_a = df_a[['success', 'month_year', 'gateway']]
df_b = df[(df['gateway'] == 'GB') & (df['transaction_type'] == 'Purchase') & (df['year'] > 2013)]
df_b = df_b[['success', 'month_year', 'gateway']]

# B.
table_a = df_a.groupby(['month_year'])['success'].mean()
table_b = df_b.groupby(['month_year'])['success'].mean()
table_a.plot(label = 'GA')
table_b.plot(label = 'GB')
plt.legend(loc='lower left', fancybox=True)

x = np.array([0,6,12,18,24, 30])
my_xticks = ['Jan14','July14','Jan15','July15', 'Jan16', 'July16']
plt.xticks(x, my_xticks)
plt.xlabel('Date')
plt.ylabel('Success Rate')
plt.title('GA vs. GB success rates for purchases 2014 - 2016')
plt.show()
plt.close()