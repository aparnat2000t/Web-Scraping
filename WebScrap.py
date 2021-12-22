#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
from bs4 import BeautifulSoup
from collections import defaultdict
URL = "https://en.wikipedia.org/wiki/A#Use_in_writing_systems"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


# In[24]:


reqData = soup.find_all('div',class_="mw-parser-output")
paragraph = soup.find_all('p')


# In[33]:


d=defaultdict(list)
i=0
for para in paragraph:
    if i >4 and i < 12:
        d["History"].append(para.text)
    elif i > 11 and i <16:
        d["Use in writing systems"].append(para.text)
    elif i > 16 and i < 23:
        d["Other uses"].append(para.text)
    i+=1


# In[36]:


for key in d:
    print(key,"\n","*"*25,"\n")
    print(d[key],"\n")


# In[ ]:




