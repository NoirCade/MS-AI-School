#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MyClass:
    pass


# In[2]:


MyClass


# In[3]:


type(MyClass)


# In[4]:


class Person:
    Name = 'Deault Name' #Perperty
    
    def Print(self):
        print('My name is {0}'.format(self.Name))


# In[5]:


son = Person()


# In[7]:


son.Name = '손흥민'
son.Print()


# In[9]:


p1 = Person()
p2 = Person()

p1.Name = '박보검'
p2.Name = '민아'

p1.Print()
p2.Print()


# In[10]:


# instance

Person.title = 'New title'


# In[11]:


p1.title


# In[12]:


p1.age = 20


# In[14]:


p2.age


# In[15]:


# 클래스의 상속

class Person:
    pass


# In[16]:


class Bird:
    pass


# In[17]:


class Student(Person):
    pass


# In[18]:


p = Person()
s = Student()


# In[20]:


isinstance(p, Person)


# In[21]:


isinstance(s, Person)


# In[22]:


isinstance(s, object)


# In[23]:


isinstance(p, Bird)


# In[31]:


# 생성자, 소멸자

class MyClass:
    #생성자
    def __init__(self, value):
        self.Value = value
        print('Class is created! Value = ', value)
        
    def __del__(self):
        print('Class is deleted')


# In[32]:


m = MyClass(10)


# In[33]:


del m


# In[34]:


# 정적 메소드
class CounterManager:
    insCount = 0
    
    def __init__(self):
        CounterManager.insCount += 1
        
    def printInstanceCount():
        print('Instance Count:', CounterManager.insCount)


# In[35]:


a, b, c = CounterManager(), CounterManager(), CounterManager()


# In[36]:


CounterManager.printInstanceCount()


# In[40]:


# 상속의 확장

class Person:
    def __init__(self, name, phone):
        self.Name = name
        self.Phone = phone
        
    def PrintInfo(self):
        print('info(Name: {0}, Phone: {1})'.format(self.Name, self.Phone))
    
    def PrintPersonData(self):
        print('Person(Name: {0}, Phone: {1})'.format(self.Name, self.Phone))


# In[52]:


class Student(Person):
    
    def __init__(self, name, phone, subject, studentID):
        self.Name = name
        self.Phone = phone
        self.Subject = subject
        self.StudentID = studentID
        
    def PrintStudentID(self):
        print(self.StudentID)


# In[53]:


p = Person('IU', '010-0000-0000')
s = Student('MinA', '010-111-1111', 'Computer Science', '0000')


# In[54]:


p.__dict__


# In[55]:


s.__dict__


# In[56]:


p.PrintInfo()


# In[57]:


s.PrintInfo()


# In[58]:


s.PrintStudentID()


# In[59]:


# 상속 관계의 확인

issubclass(Student, Person)


# In[61]:


issubclass(Person, Student)


# In[62]:


# 다중 상속

class Tiger:
    def Jump(self):
        print('Tiger Jump!!')


# In[63]:


class Lion:
    def Bite(self):
        print('Lion Bite')


# In[64]:


class Liger(Tiger, Lion):
    def Play(self):
        print('Liger Play')


# In[65]:


l = Liger()


# In[67]:


l.Play()


# In[68]:


l.Jump()


# In[69]:


l.Bite()


# In[ ]:




