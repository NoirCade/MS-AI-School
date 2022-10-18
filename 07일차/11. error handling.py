#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 12 / 0


# In[2]:


try:
    a = 12 / 0
    
except: 
    print('Error!!!')


# In[3]:


try:
    a = 12 / 0
    
except: 
    pass


# In[5]:


try:
    a = 12 / 0
    
except Exception as e:
    print('에러의 원인은', e)


# In[ ]:




