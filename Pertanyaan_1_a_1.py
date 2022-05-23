"""
Keadaan gerak setelah mencapai laju terminal?
"""
import mysql.connector as msql
# Execute query
conn = msql.connect(host='localhost', user='root',
                         password='V-k21122015', db="Euler_Methods")
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