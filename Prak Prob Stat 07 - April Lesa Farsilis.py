#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy import stats

# Data sampel
data = [9.5, 10.1, 10.2, 9.8, 10.3, 10.5, 9.5, 8.8]

# Rata-rata hipotesis
mu = 10

# Menghitung rata-rata sampel
mean_sample = np.mean(data)
print(f"Rata-rata sampel: {mean_sample}")

# Menghitung standar deviasi sampel
std_sample = np.std(data, ddof=1)
print(f"Standar deviasi sampel: {std_sample}")

# Jumlah sampel
n = len(data)

# Menghitung statistik uji t
t_statistic, p_value = stats.ttest_1samp(data, mu)
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# Menentukan taraf nyata
alpha = 0.05

# Menentukan keputusan
if p_value < alpha:
    print("Tolak hipotesis nol (H0)")
else:
    print("Gagal menolak hipotesis nol (H0)")


# In[3]:


import numpy as np
from scipy import stats

# Data sampel
data = [15000, 15500, 17500, 14500, 14000, 16000, 14500, 15500, 16500, 14000]

# Rata-rata hipotesis
mu = 14500

# Menghitung rata-rata sampel
mean_sample = np.mean(data)
print(f"Rata-rata sampel: {mean_sample}")

# Menghitung standar deviasi sampel
std_sample = np.std(data, ddof=1)
print(f"Standar deviasi sampel: {std_sample}")

# Jumlah sampel
n = len(data)

# Menghitung statistik uji t
t_statistic, p_value = stats.ttest_1samp(data, mu)
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# Menentukan taraf nyata
alpha = 0.05

# Menentukan keputusan
if p_value < alpha:
    print("Tolak hipotesis nol (H0)")
else:
    print("Gagal menolak hipotesis nol (H0)")


# In[ ]:




