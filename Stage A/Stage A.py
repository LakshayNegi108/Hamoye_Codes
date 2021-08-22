#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


A = [1,2,3,4,5,6]
B = [13, 21, 34]
A.extend(B)
print(A)


# In[4]:


a=np.eye(3)

b = np.identity(3)

print(a,"\n")
print(b,"\n")


# In[5]:


df = pd.read_csv(r"E:\python programs\DATA SCIENCE\Bijli.csv.txt",na_values = ',')
df.head(30)


# In[22]:


print(df.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean())


# In[12]:


round(df['fuel_mmbtu_per_unit'].std(),2)


# In[23]:


df['fuel_mmbtu_per_unit'].quantile(q=0.75).round(2)


# In[39]:


round(df['fuel_qty_burned'].skew(),2)


# In[41]:


round(df['fuel_qty_burned'].kurtosis(),2)


# In[77]:


print(df.isnull().sum(),"\n")
print(sum(df.isnull().sum() * 100 / len(df)))


# In[78]:


df.dtypes


# In[61]:


df0 = df['fuel_cost_per_unit_burned']
df1 = df['fuel_mmbtu_per_unit']
print(df['fuel_mmbtu_per_unit'].corr(df['fuel_cost_per_unit_burned']))
print(df['fuel_cost_per_unit_delivered'].corr(df['fuel_cost_per_unit_burned']))
print(df['report_year'].corr(df['fuel_cost_per_unit_burned']))
print(df['utility_id_ferc1'].corr(df['fuel_cost_per_unit_burned']))


# In[27]:


x = df.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()
print(x)
plt.plot(x)
plt.xlim([1995, 2000])

