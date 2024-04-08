#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 


# # The `os` Package
# 
# The `os` module provides a portable way of using operating system dependent funtionality.
# 
# Source: os Package Documentation from [https://www.python.org](python.org)

# # 1) `os.getcwd` Function
# 
# The `os.getcwd` returns the current working directory

# In[2]:


os.getcwd()


# # 2) `os.listdir` Function
# 
# The `os.listdir` function returns a list containing the names of the entries in the directory given by path

# In[3]:


os.listdir()


# # 3) `os.walk` Function
# 
# To return full path of a folder or file, we can use the `os.walk` function. `os.walk` is a generator function that returns a tuple containing : 
# 
# * The current path
# * sub-directories
# * filenames
# 
# Source :  [Mastering Python for Networking and Security](https://www.packtpub.com/product/mastering-python-for-networking-and-security/9781788992510) by José Manuel Ortega

# In[5]:


for root, dirs, files in os.walk(os.getcwd()) :
    for directory in dirs :
        print(os.path.join(root, directory))
    for file in files :
        print(os.path.join(root,file))


# # 4) Creating a Folder with `os.mkdir` Function

# In[6]:


if os.path.exists('Moon_data') == False :
    os.mkdir('Moon_data')
else :
    print("The directory already exists")


# In[7]:


os.listdir()


# In[8]:


if os.path.exists('Moon_data') == False :
    os.mkdir('Moon_data')
else :
    print("The directory already exists")


# # 5) `os.chdir` Function
# 
# The `os.chdir` function changes the directory the user is working in.

# In[9]:


os.chdir(r"C:\Users\Badr\Desktop\PYTHON\PYTHON\Moon_data")


# In[10]:


os.getcwd()


# # 6) `os.rename` Function
# 
# We can use the `os.rename` functions to move a file between directories.

# In[11]:


os.rename(r'C:\Users\Badr\Desktop\PYTHON\PYTHON\moons.csv',
          r'C:\Users\Badr\Desktop\PYTHON\PYTHON\moon_data\moons.csv')


# # 7) `os.system` Function

# In[12]:


# opening the csv file
os.system('start EXCEL.EXE moons.csv')


# In[ ]:




