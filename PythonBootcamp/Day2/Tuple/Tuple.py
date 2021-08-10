#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
fruitsname=("apple", "banana", "cherry")


# In[8]:


#access of tuple
fruitsname=("apple", "banana", "cherry")
print(fruitsname[1:])


# In[9]:


#updation
fruitsname=("apple", "banana", "cherry")
y=list(fruitsname)
y[1]='kiwi'
fruitsname=tuple(y)
print(fruitsname)


# In[10]:


#addition
#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
fruitsname=("apple", "banana", "cherry")
y=list(fruitsname)
y.append("orange")
fruitsname=tuple(y)
print(fruitsname)


# In[11]:


fruitsname=("apple", "banana", "cherry")

y=("orange",)
fruitsname += y
print(fruitsname)


# In[ ]:




