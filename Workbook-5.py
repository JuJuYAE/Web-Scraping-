#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


result = requests.get("https://example.com")


# In[3]:


type(result)


# In[4]:


result.text


# In[5]:


result.url


# In[6]:


import bs4


# In[7]:


soup = bs4.BeautifulSoup(result.text,"lxml")


# In[8]:


soup


# In[9]:


soup.select("title")[0].getText()


# In[10]:


res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")


# In[11]:


soup = bs4.BeautifulSoup(res.text,"lxml")


# In[12]:


#soup


# In[13]:


first_item = soup.select(".vector-toc-text")[1]


# In[14]:


first_item.text


# In[15]:


for item in soup.select(".vector-toc-text"): 
    print(item.text )


# In[16]:


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")


# In[17]:


res.text


# In[18]:


soup = bs4.BeautifulSoup(res.text,"lxml")


# In[19]:


#soup 


# In[20]:


soup.select(".infobox-image")


# In[21]:


computer = soup.select(".infobox-image")[0]


# In[24]:


computer 


# In[ ]:




