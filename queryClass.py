import mysql.connector


class QueryBuilder():
    def __init__(self, username, pword, db, table):
        try:
            self.data = mysql.connector.connect(
                host="127.0.0.1", port=3306, user=username, password=pword, database=db)
            tmp = self.data.cursor(buffered=True)
            tmp.execute(f"SELECT * FROM {table}")
        except Exception as error:
            if f"Unknown database '{db}'" in str(error):
                raise ValueError("Must enter valid database")

            elif f"Table '{db}.{table}' doesn't exist" in str(error):
                raise ValueError("Invalid table name")
            else:
                raise error

        self.table = table

    def insert(self, rows):
        tmp = self.data.cursor(buffered=True)
        tmp.execute(f"INSERT INTO {self.table} VALUES {rows}")
        self.data.commit()

    def delete(self, condition):
        tmp = self.data.cursor(buffered=True)
        tmp.execute(f"DELETE FROM {self.table} WHERE {condition}")
        self.data.commit()

    def update(self, set, condition):
        tmp = self.data.cursor(buffered=True)
        tmp.execute(f"UPDATE {self.table} SET {set} WHERE {condition};")
        self.data.commit()

    def addModify(self, action, column_name, data_type):
        tmp = self.data.cursor(buffered=True)

        col_info = self.columnInfo()

        if action.lower() == "modify":
            if not (column_name in [x[0] for x in col_info]):
                raise ValueError("Invalid column name")

        tmp.execute(
            f"ALTER TABLE {self.table} {action} COLUMN {column_name} {data_type}")
        self.data.commit()

    def drop(self, column_name):
        tmp = self.data.cursor(buffered=True)
        col_info = [x[0] for x in self.columnInfo()]

        if not (column_name in col_info):
            raise ValueError("Invalid column name")

        tmp.execute(
            f"ALTER TABLE {self.table} DROP COLUMN {column_name}")
        self.data.commit()

    def query(self, columns, condition=None, order_by=None):
        tmp = self.data.cursor(buffered=True)
        select_str = f"SELECT {columns} FROM {self.table}"
        if condition != None:
            select_str += f"WHERE {condition}"
        if order_by != None:
            select_str += f"ORDER BY {order_by}"
        tmp.execute(select_str)

    def columnInfo(self):
        tmp = self.data.cursor(buffered=True)
        tmp.execute(f"SELECT * FROM {self.table}")
        column_info = [[i[0], i[1], i[6]] for i in tmp.description]

        return column_info

    def getTableNames(self):
        tmp = self.data.cursor(buffered=True)
        tmp.execute("SHOW TABLES")
        return [x[0] for x in tmp]
