#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


data = pd.read_csv("D:\dataset.csv")


# In[10]:


data


# In[11]:


data.head()


# In[12]:


data.tail(5)


# In[14]:


data.Salary.plot()


# In[15]:


data.plot()


# In[16]:


data.describe()


# In[ ]:




