#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np 
from scipy.stats import t 
from scipy import stats

# Mengambil data volume dari DataFrame 
df = pd.read_clipboard()
volume = df['Volume']

# Menghitung rata-rata dan standar deviasi sampel
mean_volume = np.mean (volume)
std_dev_volume = np.std(volume, ddof=1) # ddof-1 untuk sample standard deviation

# Menghitung jumlah data 
n = len(volume)

# Menghitung interval kepercayaan 50% 
confidence_level = 0.95
z_score = stats.norm.ppf((1 + confidence_level) / 2) 
margin_of_error = z_score * (std_dev_volume / np.sqrt(n))
lower_bound = mean_volume - margin_of_error
upper_bound = mean_volume + margin_of_error

print("Interval kepercayaan 95% untuk volume rata-rata populasi kemasan oli:") 
print(f"({lower_bound}, {upper_bound})")


# In[5]:


import pandas as pd 
import numpy as np 
from scipy.stats import t 
from scipy import stats

#Rengambil data volume dari DataFrame 
df = pd.read_clipboard()
volume = df['Volume']

#Menghitung rata-rata dan standar deviasi sampel
mean_volume = np.mean (volume)
std_dev_volume = np.std(volume, ddof=1) # ddof-1 untuk sample standard deviation

#Menghitung jumlah data 
n = len(volume)

#Menghitung interval kepercayaan 50% 
confidence_level = 0.5 
z_score = stats.norm.ppf((1 + confidence_level) / 2) 
margin_of_error = z_score * (std_dev_volume / np.sqrt(n))
lower_bound = mean_volume - margin_of_error
upper_bound = mean_volume + margin_of_error

print("Interval kepercayaan 50% untuk volume rata-rata populasi kemasan oli:") 
print(f"({lower_bound}, {upper_bound})")


# In[ ]:




