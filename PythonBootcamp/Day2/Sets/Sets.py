#!/usr/bin/env python
# coding: utf-8

# ### Sets

# In[8]:


#Sets are used to store multiple items in a single variable.
#A set is a collection which is both unordered and unindexed.
#Sets are written with curly brackets.

myset={"red", "blue", "green"}


# In[6]:


#access a set
myset={"red", "blue", "green"}
for x in myset:
    print (x)


# In[7]:


#addition in sets
myset={"red", "blue", "green"}
myset.add("pink")
print(myset)

