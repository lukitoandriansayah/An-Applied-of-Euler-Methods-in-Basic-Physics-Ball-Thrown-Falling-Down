#Membuat database di mysql
"""
Dalam kasus ini, saya akan membuat database dalam
local host saya dengan menggunakan pandas. Adapun
kode yang digunakan adalah sebagai berikut
"""
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='***', user='***',
                         password='***')              # Ganti tanda *** Dengan karakter SQL masing-masing
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE Euler_Methods")
        print("Euler_Methods database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
