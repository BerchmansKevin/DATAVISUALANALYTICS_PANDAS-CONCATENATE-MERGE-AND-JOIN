#!/usr/bin/env python
# coding: utf-8

# # `BERCHMANS KEVIN S`
# 
# 

# # PANDAS CONCATENATE, MERGE AND JOIN

# Import necessary modules

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# First column should be used as the row index by passing the argument index_col=0

# In[2]:


north_america = pd.read_csv("north_america_2000_2010.csv", index_col=0)
south_america = pd.read_csv('south_america_2000_2010.csv', index_col=0)


# In[3]:


north_america


# In[4]:


north_america.shape


# In[5]:


north_america.describe()


# In[6]:


north_america.info()


# In[7]:


south_america


# In[8]:


south_america.shape


# In[9]:


south_america.describe()


# In[10]:


south_america.info()


# # Create line graphs for our yearly labor trends in north_america

# In[11]:


north_america.plot()


# # Plot transposed line graph of north_americadataframe, with title "Average Labor Hours Per Year"

# In[12]:


north_america.transpose().plot(title="Average Labour Hours Per Year")


# # Similarly, plot transposed south_america dataframe with title "Average Labor Hours Per Year". Output
# chart is shown below

# In[13]:


south_america.transpose().plot(title="Average Labour Hours Per Year")


# # Concatenate America Data

# # Concatenate north_america and south_america dataframes and store result in a dataframe, americas

# In[14]:


americas = pd.concat([north_america,south_america])


# In[15]:


americas


# # Load the additional files

# In[16]:


americas_dfs = [americas]

for year in range(2011, 2016):
    filename = "americas_{}.csv".format(year)
    df = pd.read_csv(filename, index_col=0)
    americas_dfs.append(df)


# In[17]:


americas_dfs[1]


# In[18]:


americas_dfs[2]


# # Concatenate americas and americas_dfs dataframes and store result in americas

# In[19]:


americas = pd.concat(americas_dfs, axis=1)


# In[20]:


americas.index.names = ['Country']


# In[21]:


americas


# # Now, plot transposed americas dataframe

# In[22]:


americas.transpose().plot(title="Average Labour Hours Per Year")


# # Appending data from other Continents

# In[23]:


asia = pd.read_csv('asia_2000_2015.csv', index_col=0)


# In[24]:


asia


# In[25]:


europe = pd.read_csv('europe_2000_2015.csv', index_col=0)


# In[26]:


europe.head()


# In[27]:


south_pacific = pd.read_csv('south_pacific_2000_2015.csv', index_col=0)


# In[28]:


south_pacific


# # Append asia,europe and south_pacific to americas dataframe and assign to new dataframe world 

# In[29]:


world = americas.append([asia,europe,south_pacific])


# In[30]:


world.index


# # Plot,Transpose world dataframe

# In[31]:


world.transpose().plot(title="Average Labour Hours Per Year")


# # let us customize this plot, so that country names appear outside the chart

# In[32]:


world.transpose().plot(figsize=(10,10), colormap ='rainbow',linewidth=2,title="Average Labour Hours Per Year")

plt.legend(loc='right',bbox_to_anchor=(1.3,0.5))

plt.show()


# # Merging Historical Labor Data

# In[33]:


historical = pd.read_csv('historical.csv', index_col=0)


# In[34]:


historical.head()


# In[35]:


print("World rows & columns: ", world.shape)
print("Historical rows & columns: ",historical.shape)


# # Merging historical dataframe with world dataframe and store in a new variable, world_historical

# In[36]:


world_historical = pd.merge(historical,world,left_index=True,right_index=True,how='right')


# # Print size of world_historical dataframe

# In[37]:


world_historical.shape


# # Print top-5 of world_historical dataframe

# In[38]:


world_historical.head(5)


# # Joining Historical Data

# # Use join method to join historical dataframe and world dataframe and store result in world_historical dataframe

# In[39]:


world_historical = historical.join(world,how='right')


# In[40]:


world_historical.head()


# # Plot our world labor data

# In[41]:


world_historical.sort_index(inplace=True)


# # Plot, trasposed world_historical dataframe

# In[42]:


world_historical.sort_index(inplace=True)

world_historical.transpose().plot(figsize=(15,10), colormap ='rainbow',linewidth=2,title="Average Labour Hours Per Year")

plt.legend(loc='right',bbox_to_anchor=(1.15,0.5))

plt.show()


# In[43]:


work=world.mean(axis=1)

long=max(world.mean(axis=1))

short=min(world.mean(axis=1))


# # Which country worked longer hours per year?

# In[44]:


print("Country worked longer hours per year:",work[work==long].index[0])


# # Which countryworked shorter hours per year?

# In[45]:


print("Country worked shorter hours per year:",work[work==short].index[0])


# In[ ]:




