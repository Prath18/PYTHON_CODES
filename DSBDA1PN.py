#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
iris = pd.read_csv(r"C:\Users\Dell\Downloads\iris_dataset.csv", header=None)
col_names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Species']
iris.columns = col_names
df1 = iris 
print(iris.head(8))


# In[14]:


iris.tail()


# In[15]:


iris.index


# In[16]:


iris.columns


# In[17]:


iris.shape


# In[18]:


iris.dtypes


# In[19]:


iris.describe()


# In[20]:


iris.columns.values


# In[21]:


iris.iloc[5]


# In[22]:


iris[47:51]


# In[23]:


iris.loc[:,["Sepal_Length","Sepal_Width"]]


# In[25]:


cols_2_4=iris.columns[2:4] 
iris[cols_2_4]


# In[26]:


iris.isnull().any()


# In[27]:


iris.isnull().sum()


# In[29]:


df=iris
df['petal Length(cm)']=iris['Petal_Length'].astype("int")
df1=df 
df


# In[32]:


from sklearn import preprocessing 
min_max_scaler = preprocessing.MinMaxScaler()
X=iris.iloc[:,:4] 
X


# In[33]:


X_scaled = min_max_scaler.fit_transform(X)
df_normalized = pd.DataFrame(X_scaled) 
df_normalized


# In[45]:


import pandas as pd
from sklearn.preprocessing import OneHotEncoder
df2 = df.copy()
encoder = OneHotEncoder(sparse=False) 
species_encoded = encoder.fit_transform(df2[['Species']])
encoded_df = pd.DataFrame(species_encoded, columns=encoder.categories_[0])
df2 = pd.concat([df2.drop('Species', axis=1), encoded_df], axis=1)
print(df2.head())


# In[47]:


from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(sparse=False)
df_encoded = pd.concat([df.drop('Species', axis=1), 
pd.DataFrame(enc.fit_transform(df[['Species']]), columns=enc.categories_[0])], axis=1)
print(df_encoded.head())


# In[ ]:




