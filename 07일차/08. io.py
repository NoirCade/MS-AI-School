#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('Hello World')


# In[5]:


import sys


# In[7]:


print('Welcome to', ' Python', file=sys.stderr)


# In[8]:


f = open('test.txt', 'w')


# In[10]:


print('file write', file=f)
f.close()


# ## File IO
# file 입출력을 다루다 보면 print를 사용할 수도 있지만, open을 사용하는 것이 좋다

# In[13]:


f = open('text.txt', 'w')
f.write('plow deep\nwhile sluggards sleep')
f.close()


# In[15]:


f = open('text.txt', 'r')
f.read()
f.close()


# In[ ]:




