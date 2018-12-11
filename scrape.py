#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[60]:


def get_pct_counts(year):
    print(year)
    df = pd.read_csv(f"../data/raw/{year}.csv", encoding="cp1252")
    return df.groupby(["year", "pct", "race"])["ser_num"].count()


# In[61]:


df = pd.concat(get_pct_counts(y) for y in range(2003, 2017))


# In[62]:


df


# In[65]:


r_df = pd.DataFrame(df).rename(columns={"ser_num":"count"})
r_df["race"] = r_df["race"].map({"":"NOT LISTED","A":"ASIAN/PACIFIC ISLANDER","B":"BLACK","I":"AMERICAN INDIAN/ALASKAN NATIVE",
"P":"BLACK-HISPANIC","Q":"WHITE-HISPANIC","W":"WHITE","X":"UNKNOWN","Z":"OTHER"})


# In[67]:





# In[59]:


df = pd.read_csv("../data/ra")


# In[68]:




