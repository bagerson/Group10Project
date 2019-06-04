#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Dependencies
import pandas as pd


# In[4]:


# Store filepath in a variable
file_one = "Resources/DJIA.csv"
file_two = "Resources/NASDAQ100.csv"
file_three = "Resources/SP500.csv"
file_four = "Resources/HPI_master.csv"


# In[6]:


# Read our Data files with the pandas library
#create dataframes
DJIA_df = pd.read_csv(file_one)
DJIA_df.head()


# In[7]:


NAS_df = pd.read_csv(file_two)
NAS_df.head()


# In[9]:


SP500_df = pd.read_csv(file_three)
SP500_df.head()


# In[10]:


HPI_df = pd.read_csv(file_four)
HPI_df.head()


# In[ ]:




