"""
Keadaan gerak saat 0.99 laju terminal?
"""
import mysql.connector as msql
# Execute query
conn = msql.connect(host='***', user='***',
                         password='***', db="Euler_Methods")      #Ubah *** sesuai karakter MySQL masing-masing
cursor = conn.cursor()
t_when_v_is_v_term = "SELECT t, x, v, a " \
                     "FROM Euler_Method_No_1_b_1 " \
                     "WHERE v >= 0.99 * 150 * (1000/3600) " \
                     "limit 1"
cursor.execute(t_when_v_is_v_term)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
