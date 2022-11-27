import mysql.connector
from queryClass import *

cnx = mysql.connector.connect(
    host="127.0.0.1", port=3306, user="root", password="R6clolvalrr.#")


obj = QueryBuilder("root", "R6clolvalrr.#", "olympicarchery", 'country')

obj.drop("AllTimeDubs")
# print(cur.fetchall())
# table = "olympicarchery.coach"

# columns = [i[0] for i in cur.description]

# obj = QueryBuilder(cnx, table)
