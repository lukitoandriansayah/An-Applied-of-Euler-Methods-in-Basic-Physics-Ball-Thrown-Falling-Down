"""
Berapa Ketidakpastian laju setalah 10 detik tersebut?

Untuk meneyelesaikan ini, kita bandingkan data utama dengan data pembanding.
"""
import mysql.connector as msql
# Execute query
conn = msql.connect(host='***', user='***',
                         password='***', db="Euler_Methods")      #Ubah *** sesuai karakter MySQL masing-masing
cursor = conn.cursor()
v_after_10_s = "SELECT distinct " \
               "em1a1.v," \
               " " \
               "em1a2.v, abs(1-(em1a2.v/em1a1.v))*100 as KetidakPastian " \
               "FROM " \
               "euler_methods.euler_method_no_1_a_1 as em1a1, " \
               "euler_methods.euler_method_no_1_a_2 as em1a2 " \
               "WHERE ( em1a1.t >= 10 and em1a2.t >= 10 )" \
               "and round(em1a1.t,5) = round(em1a2.t,5) " \
               "limit 1"
cursor.execute(v_after_10_s)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
