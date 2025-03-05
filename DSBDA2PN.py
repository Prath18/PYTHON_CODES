#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats 
file_path = r"C:\Users\Dell\Desktop\studentdata.csv.xlsx"
df = pd.read_excel(file_path)
df.head(20)


# In[17]:


df.isnull()


# In[20]:


print(df.columns)


# In[24]:


series1 = pd.notnull(df["Reading_Score "]) 
df[series1]


# In[25]:


ndf=df 
ndf.fillna(0)


# In[26]:


m_v=df['Reading_Score '].mean()
df['Reading_Score '].fillna(value=m_v, inplace=True)
df


# In[27]:


ndf.dropna(how = 'all')


# In[28]:


ndf.dropna(axis = 1)


# In[29]:


new_data =ndf.dropna (axis = 0, how ='any') 
new_data


# In[35]:


col =['Reading_Score ', 'Reading_Score ', 'Writing_Score '] 
df.boxplot(col)


# In[ ]:




