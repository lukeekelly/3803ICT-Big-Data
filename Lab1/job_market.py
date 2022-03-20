#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as numpy


# In[5]:


# Load the data using Pandas
df = pd.read_csv('job-market.csv')
print("The Dataset consists of: ", ..., " rows and ", ..., " columns")

#TODO: Visualize the top 10 first Rows
df.head(10)


# In[3]:


df.dtypes


# In[7]:


#TODO: fix the data type of column Date
df["Date"] = pd.to_datetime(df["Date"])

df.dtypes


# In[10]:


# Calculate the average salary as a new column
df = df.assign(AverageSalary = df['HighestSalary'] - df['LowestSalary'])

df.head(10)


# In[ ]:




