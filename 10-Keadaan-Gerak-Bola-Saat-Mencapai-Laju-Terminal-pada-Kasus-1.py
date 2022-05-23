"""
Keadaan gerak setelah mencapai laju terminal?

Keadaan gerak di sini mencaku waktu, posisi, laju, dan percepatan.
"""
import mysql.connector as msql
# Execute query
conn = msql.connect(host='***', user='***',
                         password='***', db="Euler_Methods")  #Ubah *** sesuai karakter MySQL masing-masing
cursor = conn.cursor()
coord_v_term = "SELECT t, x, v, a " \
               "FROM Euler_Method_No_1_a_1 " \
               "WHERE v >= 150*(1000/3600) " \
               "Limit 1"
cursor.execute(coord_v_term)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
