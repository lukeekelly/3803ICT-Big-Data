#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import re


# #### Import the data and get a high-level picture

# In[238]:


df = pd.read_csv('sales.csv')
df.head()


# In[239]:


df.shape


# In[240]:


df.dtypes


# #### TODO: Fix column datatypes
# 
# Change ordered_at to datetime
# 
# Change price and line_total to float

# In[241]:


df['ordered_at'] = df['ordered_at'].apply(pd.to_datetime) 


# In[242]:


df['line_total'] = pd.to_numeric(df['line_total'], errors = 'coerce')
df['price'] = pd.to_numeric(df['price'],  errors = 'coerce')


# In[243]:


df.dtypes


# #### TODO: drop if duplicated or null

# In[244]:


df[df.duplicated()].shape[0]


# In[245]:


df = df.drop_duplicates()


# In[246]:


df.isnull().sum()


# In[247]:


df[df['name'].isnull()].head()


# In[248]:


df = df.dropna(how='any',axis=0) 


# #### Sanity check for value ranges and to check assumptions

# In[249]:


df[(df['price'] * df['quantity']) != df['line_total']].shape[0]


# In[250]:


df[df['line_total'] < 0].shape[0]


# #### TODO: 
# Set line_total = price * quantity if different
# Remove if line total < 0

# In[251]:


df['line_total'] = df['price'] * df['quantity']


# In[252]:


index_names = df[df['line_total'] < 0 ].index
df.drop(index_names , inplace=True)


# In[253]:


df.describe()


# #### TODO: Get value between "" in name and put it in category column

# In[232]:


df1 = df['name']


# In[233]:


df.head()


# #### Analysis, finally!

# In[254]:


f, ax = plt.subplots(figsize=(10, 6))
df.groupby('name')['line_total'].sum().sort_values(ascending=False).head(10).plot(kind='bar')
f.autofmt_xdate()
plt.show()


# In[ ]:




