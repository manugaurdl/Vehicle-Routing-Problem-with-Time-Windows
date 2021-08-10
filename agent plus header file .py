#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np


# In[14]:


MAX_LABEL_COST =  99999
_MAX_NUMBER_OF_NODES = 3000
_MAX_NUMBER_OF_LINKS = 6000
_MAX_NUMBER_OF_TIME_INTERVALS = 200

_MAX_NUMBER_OF_VEHICLES = 40
_MAX_NUMBER_OF_PASSENGERS = 2000
_MAX_NUMBER_OF_SERVED_PASSENGERS = 20

_MAX_NUMBER_OF_STATES =300

g_number_of_passengers = None


_MAX_NUMBER_OF_OUTBOUND_NODES =  10



# In[35]:


#Initialising 2d Array 
def _2D(x, y):
    return np.zeros(x,y)


# In[36]:


#Initialising 3d Array 
def _3D(x,y,z):
    return np.zeros((x,y,z))


# In[37]:


#Initialising 4d Array 
def _4D(w,x,y,z):
    return np.zeros((w,x,y,z))


# In[38]:


#Initialising 5d Array 
def _5D(v,w,x,y,z):
    return np.zeros((v,w,x,y,z))


# In[ ]:


#extern bool g_Optimization_Lagrangian_Method_Vehicle_Routing_Problem_Simple_Variables();  // with varaible y only;


# In[ ]:




