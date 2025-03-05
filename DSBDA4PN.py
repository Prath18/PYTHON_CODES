#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
x=np.array([95,85,80,70,60])
y=np.array([85,95,70,65,70])
model=np.polyfit(x, y, 1)
model


# In[2]:


predict=np.poly1d(model) 
predict(65)


# In[3]:


y_pred= predict (x)
y_pred


# In[4]:


from sklearn.metrics import r2_score
r2_score(y, y_pred)


# In[5]:


y_line= model[1] + model[0]*x
plt.plot(x, y_line, c='r') 
plt.scatter(x, y_pred)
plt.scatter(x, y, c='r')


# In[6]:


from sklearn.datasets import fetch_openml
from sklearn.datasets import fetch_california_housing 
housing = fetch_california_housing()
housing


# In[7]:


data = pd.DataFrame(fetch_california_housing().data) 
data.columns =fetch_california_housing().feature_names
data.head()


# In[8]:


df=pd.DataFrame(housing.data, columns=housing.feature_names) 
df


# In[9]:


data['PRICE'] = housing.target
data.isnull().sum()


# In[35]:


x = data.drop(['PRICE'], axis = 1)
y = data['PRICE']
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size
=0.2,random_state = 0) 
import sklearn
from sklearn.linear_model import LinearRegression 
lm = LinearRegression()
model=lm.fit(xtrain, ytrain)
ytrain_pred = lm.predict(xtrain)
ytest_pred = lm.predict(xtest)
df=pd.DataFrame(ytrain_pred,ytrain)
df=pd.DataFrame(ytest_pred,ytest)
from sklearn.metrics import mean_squared_error,r2_score 
mse = mean_squared_error(ytest, ytest_pred)
print(mse) 


# In[36]:


mse = mean_squared_error(ytrain_pred,ytrain) 
print(mse)


# In[37]:


plt.scatter(ytrain ,ytrain,c='blue',marker='o',label='Training data')


# In[25]:


plt.scatter(ytest,ytest_pred ,c='lightgreen',marker='s',label='Test data')


# In[28]:


plt.scatter(ytrain ,ytrain,c='blue',marker='o',label='Training data')
plt.scatter(ytest,ytest_pred ,c='lightgreen',marker='s',label='Test data')
plt.xlabel('True values')
plt.ylabel('Predicted')
plt.title("True value vs Predicted value")
plt.legend(loc= 'upper left')
plt.plot()
plt.show()


# In[ ]:




