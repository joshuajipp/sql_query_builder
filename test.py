import mysql.connector
from queryClass import *
from displayData import *

cnx = mysql.connector.connect(
    host="127.0.0.1", port=3306, user="root", password="Mx.ze0218")


#obj = QueryBuilder("root", "R6clolvalrr.#", "olympicarchery", 'country')

#obj.drop("AllTimeDubs")
# print(cur.fetchall())
# table = "olympicarchery.coach"

# columns = [i[0] for i in cur.description]

# obj = QueryBuilder(cnx, table)
column =  ['name', 'kids']
row = [('gerry', 3),('lingling', 1),('rowena',3)]
displayTable(column, row)