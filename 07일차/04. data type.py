#!/usr/bin/env python
# coding: utf-8

# In[3]:


# List
a_list = [1,2,3,4,5]

print(a_list)
print(a_list[0])
print(a_list[1])


# In[5]:


# 슬라이싱
print(a_list[:2])


# In[6]:


print(a_list[2:])


# In[7]:


print(a_list[:])


# In[9]:


print(a_list[1::2])


# In[12]:


b = a_list[:]
b[0] = 100
print(b)


# In[13]:


print(a_list)


# In[15]:


b_list = []
b_list.append(1)
b_list.append(2)
b_list.append(3)

print(b_list)


# In[17]:


b_list.insert(2, 100)

print(b_list)


# In[18]:


# tuple
a_tuple = (1,2,3,4,5)

print(a_tuple)


# In[19]:


a_tuple[0] = 10 #튜플은 설정 후 인덱스로 호출 불가


# In[20]:


a = 100
b = 200
c = b
b = a
a = c

print(a, b)


# In[21]:


a, b = b, a

print(a, b)


# In[22]:


# Dict

a_dic = {1:'a', 'b':[1,2,3,], 'c':3}

print(a_dic)


# In[26]:


print(a_dic[1])
print(a_dic['b'])
print(a_dic['c'])


# In[28]:


a_dic['d'] = 'Microsoft AI School'
print(a_dic)


# In[31]:


# Set

a_set = {1,2,3}

print(a_set)
print(type(a_set))


# In[33]:


b_set = {3,4,5}


# In[34]:


a_set.union(b_set) #합집합


# In[35]:


a_set.intersection(b_set) #교집합


# In[36]:


a_set - b_set #차집합


# In[37]:


a_set | b_set #합집합2


# In[39]:


a_set & b_set #교집합2


# In[40]:


# 부록 - 데이터 타입 변환

a = set((1,2,3))
print(type(a))


# In[41]:


b = list(a)
print(type(b))


# In[42]:


c = tuple(b)
print(type(c))


# In[ ]:




