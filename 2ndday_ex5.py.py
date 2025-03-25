#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
array=np.array([1,2,2,3,3,3,4,4,4,4])
counts=np.bincount(array)
most_freq_value=np.argmax(counts)


# In[21]:


most_freq_value


# In[ ]:




