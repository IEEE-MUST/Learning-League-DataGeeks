#!/usr/bin/env python
# coding: utf-8

# ### LIST
# 

# In[1]:


#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets


# In[3]:


#Create a List
fruits = ["apple", "banana", "cherry"]
print(fruits)


# In[5]:


#List Items- String, int and boolean data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# In[7]:


#type()
#What is the data type of a list?

fruits = ["apple", "banana", "cherry"]
print(type(fruits))


# In[9]:


#Accessing List items
#1. Through indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2. Negetive indexing
# -1 refers to the last item, -2 refers to the second last item etc.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#3. Range of Indexes
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


# In[10]:


#List Slicing
a= ["ram", 10, "shyam", 12.5]


# In[11]:


a[0:]


# In[12]:


a[1:3]


# In[13]:


a[:]


# In[14]:


a[:4]


# In[16]:


#Changing List Items
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)


# In[18]:


#Adding List items
#1. append()
#Using the append() method to append an item:

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


#2. Insert Items
#To insert a list item at a specified index, use the insert() method.
#Insert an item as the second position:

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)


# In[ ]:


#Remove List It

