#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# Data
data = {
    "X": [40, 20, 25, 20, 30, 50],
    "Y": [385, 400, 395, 365, 475, 440]
}
df = pd.DataFrame(data)

# Menghitung rata-rata
mean_X = np.mean(df["X"])
mean_Y = np.mean(df["Y"])

# Menghitung b1 (slope)
df['XY'] = df['X'] * df['Y']
df['X^2'] = df['X'] ** 2
b1 = (sum(df['XY']) - len(df) * mean_X * mean_Y) / (sum(df['X^2']) - len(df) * mean_X ** 2)

# Menghitung b0 (intersep)
b0 = mean_Y - b1 * mean_X

# Persamaan regresi
regression_eq = f"Y = {b0:.2f} + {b1:.2f}X"

# Menghitung koefisien korelasi (r)
correlation_matrix = np.corrcoef(df["X"], df["Y"])
r = correlation_matrix[0, 1]

# Menghitung koefisien determinasi (R^2)
R2 = r ** 2

# Menampilkan hasil dengan deskripsi
print(f"Rata-rata X: {mean_X:.2f}")
print(f"Rata-rata Y: {mean_Y:.2f}")
print(f"Nilai intersep (b0): {b0:.2f}")
print(f"Nilai kemiringan (b1): {b1:.2f}")
print(f"Koefisien korelasi (r): {r:.2f}")
print(f"Koefisien determinasi (R^2): {R2:.2f}")
print(f"Persamaan regresi: {regression_eq}")

# Menampilkan DataFrame
print("\nDataFrame:")
print(df)


# In[3]:


import numpy as np
import pandas as pd

# Data
data={
    "X": [2.8,2.5,3.5,3.1,3,3.8,3.3,3.5],
    "Y": [5.4, 5.1, 7.2, 6.2, 6, 7.5, 6.8, 8.9]
}
df = pd.DataFrame(data)
 
# Menghitung rata-rata
mean_X = np.mean(df["X"])
mean_Y = np.mean(df["Y"])

# Menghitung b1 (slope)
df['XY'] = df['X'] * df['Y']
df['X^2'] = df['X'] ** 2
b1 = (sum(df['XY'])- len(df) * mean_X * mean_Y) / (sum(df['X^2'])- len(df) * mean_X ** 2)

# Menghitung b0 (intersep)
b0 = mean_Y- b1 * mean_X

# Persamaan regresi
regression_eq = f"Y = {b0:.2f} + {b1:.2f}X"

# Menghitung koefisien korelasi (r)
correlation_matrix = np.corrcoef(df["X"], df["Y"])
r = correlation_matrix[0, 1]

# Menghitung koefisien determinasi (R^2)
R2 =r ** 2

# Menampilkan hasil dengan deskripsi
print(f"Rata-rata X: {mean_X:.2f}")
print(f"Rata-rata Y: {mean_Y:.2f}")
print(f"Nilai intersep (b0): {b0:.2f}")
print(f"Nilai kemiringan (b1): {b1:.2f}")
print(f"Koefisien korelasi (r): {r:.2f}")
print(f"Koefisien determinasi (R^2): {R2:.2f}")
print(f"Persamaan regresi: {regression_eq}")

# Menampilkan DataFrame
print("\nDataFrame:")
print(df)


# In[ ]:





# In[ ]:




