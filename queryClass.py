import mysql.connector


class QueryBuilder():
    def __init__(self, username, pword, db, table):
        try:
            tmp = mysql.connector.connect(
                host="127.0.0.1", port=3306, user=username, password=pword, database=db)
            self.db = tmp.cursor()
            self.db.execute(f"SELECT * FROM {table}")
        except Exception as error:
            if "Unknown database" in str(error):
                raise ValueError("Must enter valid database")
                # raise ValueError("Invalid database")
            elif f"Table '{db}.{table}' doesn't exist" in str(error):
                raise ValueError("Invalid table name")
            else:
                raise error

        self.table = table

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def alter(self):
        pass

    def query(self):
        pass
