#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
file_path = r"C:\Users\Dell\Desktop\customer.csv.xlsx"
df = pd.read_excel(file_path)
df.head()


# In[3]:


df.info()


# In[4]:


df.head


# In[5]:


df.tail


# In[6]:


df.describe()


# In[7]:


df.Age.mean() 


# In[8]:


df.Age.mode()


# In[9]:


df.Age.median()


# In[10]:


df.groupby(['Age']).count()


# In[13]:


print(df.columns)


# In[14]:


df[['Age' , 'Annual Income($)\t', 'Spending Score\t']].mean()


# In[15]:


df[['Age' , 'Annual Income($)\t', 'Spending Score\t']].mode()


# In[16]:


df[['Age' , 'Annual Income($)\t', 'Spending Score\t']].median()


# In[17]:


df[['Age' , 'Annual Income($)\t', 'Spending Score\t']].max()


# In[18]:


df[['Age' , 'Annual Income($)\t', 'Spending Score\t']].std()


# In[22]:


df2 = df.groupby('Gender')
df


# In[23]:


for Gender, Gender_f in df2: 
    print(Gender)
    print(Gender_f)


# In[25]:


df2.get_group('Male')


# In[26]:


df2.get_group('Female')


# In[ ]:




