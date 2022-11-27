import mysql.connector
from queryClass import *


def validateCredentials(username, pword) -> bool:
    try:
        mysql.connector.connect(
            host="127.0.0.1", port=3306, user=username, password=pword)
    except Exception as error:
        if "Access denied for user" in str(error):
            print("Invalid Login Credentials")
            return False
        else:
            raise error
    return True

def validateOperation(option):
    operations = ["a","b","c","d","e","f","g"]
    if option.lower() in operations:
        return True
    return False
    
def validateTable(username, password, schema, table_name):
    obj = QueryBuilder(username, password, schema, table_name)
    if table_name in table_names:
            new_data = obj.delete(table_name, condition)
    else 
    

