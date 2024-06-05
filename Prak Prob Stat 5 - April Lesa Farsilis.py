#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.stats import norm

# Menentukan rata-rata dan standar deviasi
mean = 184 # rata-rata
std_dev = 5 # standar deviasi

# Menghitung probabilitas tinggi kurang dari 189 cm
height = 189
prob_less_than_189 = norm.cdf(height, mean, std_dev)

# Menampilkan hasil
print("Probabilitas tinggi yang kurang dari 189 cm:", prob_less_than_189)


# In[1]:


from scipy.stats import norm

# Menentukan rata-rata dan standar deviasi
mean = 184 # rata-rata
std_dev = 5 # standar deviasi

# Menghitung probabilitas tinggi kurang dari 174 cm
prob_less_than_174 = norm.cdf(174, mean, std_dev)

# Menghitung probabilitas tinggi kurang dari 199 cm
prob_less_than_199 = norm.cdf(199, mean, std_dev)

# Kemungkinan antara 174 cm dan 199 cm adalah selisih antara probabilitas kurang dari 199 dan kurang dari 174
prob_between_174_and_199 = prob_less_than_199 - prob_less_than_174

# Menampilkan hasil
print("Probabilitas tinggi antara 174 cm dan 199 cm:", prob_between_174_and_199)


# In[3]:


from scipy.stats import norm

# Menentukan rata-rata dan standar deviasi
mean = 173 # rata-rata
std_dev = 34 # standar deviasi

# Menghitung probabilitas apel berkualitas "not good" (berat kurang dari 120 gram)
prob_not_good = norm.cdf(120, mean, std_dev)

# Menampilkan hasil
print("Peluang apel yang berkualitas 'not good': {:.4f}".format(prob_not_good))


# In[4]:


# Definisi laju kedatangan dan laju pelayanan
arrival_rate = 1/10 # pelanggan per menit
service_rate = 1/8 # pelanggan per menit

# Menghitung rata-rata jumlah pelanggan dalam sistem (L)
L = arrival_rate / (service_rate - arrival_rate)

# Menghitung rata-rata waktu setiap pelanggan berada dalam sistem (W)
W = L / arrival_rate

# Menampilkan hasil
print("Rata-rata jumlah pelanggan dalam sistem (L): {:.2f}".format(L))
print("Rata-rata waktu setiap pelanggan berada dalam sistem (W): {:.2f}".format(W))


# In[5]:


from scipy.stats import expon

# Rerata waktu pelayanan (mu)
mean_service_time = 7  # menit

# Menghitung peluang seseorang dilayani antara 3 sampai 5 menit
prob_between_3_and_5 = expon.cdf(5, scale=mean_service_time) - expon.cdf(3, scale=mean_service_time)

# Menampilkan hasil
print("Peluang seseorang dilayani antara 3 sampai 5 menit: {:.7f}".format(prob_between_3_and_5))


# In[6]:


from scipy.stats import poisson

# Rata-rata pelanggan per menit (λ)
mean_arrival_rate = 5

# Menghitung peluang lebih dari 6 pelanggan tiba dalam periode 2 menit
prob_more_than_6_arrivals = 1 - poisson.cdf(6, mu=mean_arrival_rate * 2)

# Menampilkan hasil
print("Peluang lebih dari 6 pelanggan akan tiba dalam periode 2 menit berikutnya: {:.7f}".format(prob_more_than_6_arrivals))


# In[9]:


from scipy.stats import norm

# Menentukan rata-rata dan standar deviasi
mean = 184 # rata-rata
std_dev = 5 # standar deviasi

# Probabilitas tinggi lebih tinggi dari tinggi tertentu
prob_more_than = 1 - 0.1685

# Menggunakan fungsi quantile untuk menemukan tinggi yang sesuai
height = norm.ppf(prob_more_than, mean, std_dev)

# Menampilkan hasil
print("Tinggi sedemikian rupa sehingga 16,85% pemain basket lebih tinggi dari {:.2f} cm".format(height))


# In[8]:


from scipy.stats import binom

# Menentukan parameter distribusi binomial
n = 8 # total jumlah apel
p = 0.06 # probabilitas apel berkualitas "not good"

# Menghitung probabilitas jumlah apel berkualitas "not good" kurang dari atau sama dengan 2
prob_not_good_2_or_less = binom.cdf(2, n, p)

# Menampilkan hasil
print("Probabilitas kurang dari atau sama dengan 2 apel berkualitas 'not good': {:.7f}".format(prob_not_good_2_or_less))


# In[7]:


# Definisi laju kedatangan dan laju pelayanan
arrival_rate_new = 1/16  # pelanggan per menit

# Menghitung ulang rata-rata jumlah pelanggan dalam sistem (L)
L_new = arrival_rate_new / (service_rate - arrival_rate_new)

# Menghitung ulang rata-rata waktu setiap pelanggan berada dalam sistem (W)
W_new = L_new / arrival_rate_new

# Menampilkan hasil
print("Rata-rata jumlah pelanggan dalam sistem (L) setelah perubahan: {:.2f}".format(L_new))
print("Rata-rata waktu setiap pelanggan berada dalam sistem (W) setelah perubahan: {:.2f}".format(W_new))


# In[11]:


from scipy.stats import expon

# Rerata waktu pelayanan (mu)
mean_service_time = 7  # menit

# Menghitung peluang seseorang mendapatkan pelayann lebih dari 8 menit
prob_more_than_8_minutes = 1 - expon.cdf(8, scale=mean_service_time)

# Menampilkan hasil
print("Peluang seseorang mendapatkan pelayanan lebih dari 8 menit: {:.7f}".format(prob_more_than_8_minutes))


# In[10]:


from scipy.stats import poisson

# Rata-rata pelanggan per menit (λ)
mean_arrival_rate = 5

# Menghitung peluang tepat 4 pelanggan akan datang dalam 1 menit
prob_4_arrivals = poisson.pmf(4, mu=mean_arrival_rate)

# Menampilkan hasil
print("Peluang bahwa dalam 1 menit berikutnya terdapat tepat 4 pelanggan yang akan datang: {:.7f}".format(prob_4_arrivals))


# In[12]:


# Rata-rata pelanggan per menit (λ)
mean_arrival_rate = 5

# Menghitung rata-rata jumlah kedatangan selama periode 1 jam
mean_arrivals_per_hour = mean_arrival_rate * 60  # 60 menit dalam satu jam

# Menampilkan hasil 
print("Rata-rata jumlah kedatangan selama periode 1 jam: {:.2f}".format(mean_arrivals_per_hour))


# In[ ]:




