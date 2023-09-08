#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[40]:


import numpy as np


# #### Create an array of 10 zeros 

# In[41]:


np.zeros(10)


# #### Create an array of 10 ones

# In[42]:


np.ones(10)


# #### Create an array of 10 fives

# In[7]:


array = [5]*10
print(array)


# In[43]:


np.ones(10)*5


# In[44]:


np.zeros(10)+5


# #### Create an array of the integers from 10 to 50

# In[45]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[10]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[46]:


matrix = np.arange(9).reshape(3,3)
print(matrix)


# #### Create a 3x3 identity matrix

# In[47]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[49]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[15]:


np.random.randn(25)


# #### Create the following matrix:

# In[50]:


np.arange(1,101).reshape(10,10)/100


# In[52]:


np.linspace(0.01,1,100).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[24]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[53]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[70]:


mat[2:,1:]


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[72]:


mat[3,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[81]:


mat[:3,1:2]


# # WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# # BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# # BE ABLE TO SEE THE OUTPUT ANY MORE

# In[82]:


mat[4,:]


# In[84]:


mat[-1,:]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[85]:


mat


# In[87]:


mat[3:5,:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[88]:


mat


# In[89]:


np.sum(mat)


# In[90]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[92]:


np.std(mat)


# In[93]:


mat.std()


# #### Get the sum of all the columns in mat

# In[94]:


mat.sum(axis=0)


# In[53]:





# # Great Job!
