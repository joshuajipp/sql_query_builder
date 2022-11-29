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
    operations = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if option.lower() in operations:
        return True
    return False


def validateTable(table_name, tables_list):
    if table_name.lower() in tables_list:
        return True
    return False


def validateColumnInput(inp, col_info):
    if inp == '' and col_info[2] == 0:
        return f'Column "{col_info[0]}" cannot be NULL'
    if col_info[1] == 3 and inp != '':
        try:
            int(inp)
        except ValueError:
            return f'Column "{col_info[0]}" must be an integer'
    if col_info[1] == 254 and len(inp) > 1:
        return f'Column "{col_info[0]}" must not be more than 1 character'

    return True


# def validateCondition():
#     if
