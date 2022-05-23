"""
PERHATIAN!!!
Silakan simpan file ini dengan nama Data_1_a_1 dalam format .py
untuk memudahkan.
"""


import pandas as pd
import numpy as np

"""Known Variables in SI units for Case 1"""
v_0 = 35 * (1000/3600)
v_term = 150 * (1000/3600)
t_total = float(10)                         #t_total di sini adalah waktu yang diketahui dalam data bukan waktu secara keseluruhan
t_df = t_total + 0.01                       #Penggunaan 0.01 optional
"""
Using Methode Euler
"""
t_0 = 0
x_0 = 0
a_0 = float(9.81)                       #variabel a_0 disini merupakan nilai percepatan gravitasi bumi
n = 5000                                #Pemilihan nilai n optional, karena ini akan digunakan sebagai acuan banyaknya jumlah baris data yang ingin dibuat dalam dataframe
dt = 6 * t_df / n                       #Penggunaan angka 6 adalah optional, semakin besar semaik baik

#Step1: Membuat kerangka data frame
data =[t_0, x_0, v_0]
data.append(a_0*(1-(data[2]**2/v_term**2)))
rows = [0]
while n not in rows:
    rows.append(rows[-1] + 1)
index = np.array(rows)
df = pd.DataFrame(columns=['t','x','v','a'], index= index)
df.loc[0] = data

#Step2: Melengkapi Kerangka Dataframe
i = 1
while np.isnan(df['t'].loc[i]).sum() > 0 and i < n:
    df['v'].loc[i] = df['v'].loc[i - 1] + (df['a'].loc[i - 1] * dt)
    df['x'].loc[i] = df['x'].loc[i - 1] + (df['v'].loc[i - 1] * dt)
    df['t'].loc[i] = df['t'].loc[i-1]+dt
    df['a'].loc[i] = a_0 * (1 - (df['v'].loc[i] ** 2 / v_term ** 2))
    i += 1
df_euler_methods = df.dropna(axis=0)
df_euler_methods.to_csv('Data Frame Nomor 1_a_1.csv', index=False, encoding='utf-8', quoting=1)

#Step3: Mengimport DataFrame ke dalam DataBase MySQL
from sqlalchemy import create_engine
import pymysql
import mysql
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                      .format(user="***", pw="***",
                      db="Euler_Methods"))  # Ubah *** sesuai karakter MySQL masing-masing
df_euler_methods.to_sql('Euler_Method_No_1_a_1', con = engine, if_exists = 'append', chunksize = 1000,index=False)
