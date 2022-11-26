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
                # raise ValueError("Invalid database")
            elif f"Table '{db}.{table}' doesn't exist" in str(error):
                raise ValueError("Invalid table name")
            else:
                raise error

        self.table = table

    def insert(self):
        pass

    def delete(self, condition):
        tmp = self.data.cursor(buffered=True)
        tmp.execute(f"DELETE FROM {self.table} WHERE {condition}")
        self.data.commit()

    def update(self):
        pass

    def alter(self):
        pass

    def query(self):
        pass

    def columnInfo(self):
        tmp = self.data.cursor(buffered=True)
        tmp.execute(f"SELECT * FROM {self.table}")
        column_nullable_dict = {i[0]: i[6] for i in tmp.description}

        return column_nullable_dict
