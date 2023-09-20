#!/usr/bin/env python
# coding: utf-8

# # The Weather Dataset 
# 

# In[1]:


import pandas as pd 


# In[3]:


data=pd.read_csv("file.csv")
data.head()


# # 1)Find all the unique "Wind Speed" values in the data.

# In[5]:


data.head(2)


# In[11]:


data.nunique()


# In[13]:


data['Wind Speed_km/h'].nunique()


# In[15]:


data['Wind Speed_km/h'].unique()


# # 2)Find the number of times when the 'Weather is exactly clear'.

# In[ ]:


#value_counts()


# In[17]:


data.head(2)


# In[25]:


data['Weather'].value_counts()


# In[27]:


#filtering
data[data.Weather=="Clear"]


# In[29]:


#groupby()
data.groupby("Weather").get_group('Clear')


# # 3)Find the number of times when the "Wind Speed was exactly 4 km?h"

# In[30]:


data.head(3)


# In[41]:


data[data['Wind Speed_km/h']==4]


# # 4)Find out all the Null Values in the data.

# In[43]:


data.isnull().sum()


# In[44]:


data.notnull().sum()


# # 5)Rename the column name 'Weather' of the dataframe to 'Weather Condition'

# In[45]:


data.rename(columns = {'Weather': 'Weather Condition'})


# In[46]:


data.head()


# In[49]:


data.rename(columns = {'Weather': 'Weather Condition'}, inplace=True)
data.head(2)


# # 6)What is the mean 'Visibility' ?

# In[51]:


data['Visibility_km'].mean()


# # 7)What is the Standard Deviation of 'Pressure' in this data?

# In[52]:


data.head(2)


# In[53]:


data['Press_kPa'].std()


# # 8)What is the Variance of 'Relative Humidity' in this data?

# In[54]:


data['Rel Hum_%'].var()


# # 9)Find all instances when 'Snow' was recorded.

# In[55]:


data.head(5)


# In[57]:


#filtering
data[data['Weather Condition']=="Snow"]


# In[58]:


#value_counts()
data['Weather Condition'].value_counts()


# In[64]:


#groupby
data.groupby('Weather Condition').get_group('Snow')


# In[ ]:


#str.contains()


# In[67]:


data[data['Weather Condition'].str.contains('Snow')].head(4)


# # 10)Find all instance when 'Wind speed is above 24' and 'Visibility is 25'.

# In[75]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km']==25)]


# # 11)What is the Mean value of each columns against each 'Weather Condition' ?

# In[79]:


data.groupby('Weather Condition').mean()


# # 12)What is the minimum and maximum value of each column against each 'Weather Condition' ?

# In[84]:


data.groupby('Weather Condition').min()


# In[85]:


data.groupby('Weather Condition').max()


# # 13)Show all the Records where Weather Condition is Fog.

# In[87]:


data[data['Weather Condition']=='Fog']


# # 14)Find all instances when 'Weather is Clear ' or 'Visibility is above 40' .

# In[92]:


data[(data['Weather Condition']=='Clear') | (data['Visibility_km'] > 40)].tail(5)


# # 14)Find all instances when:
# A) 'Weather is clear' and 'Relative Humidty is greater than 50'
# or 
# B)'Visibility is above 40'

# In[93]:


data.head(2)


# In[98]:


data[(data['Weather Condition']=='Clear') & (data['Rel Hum_%'] >50) | (data['Visibility_km'] >40)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




