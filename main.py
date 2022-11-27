import mysql.connector
from queryClass import *
from validate import *
from getpass import getpass


def main():
    schema = "olympicarchery"
    user = input("Username: ")
    password = getpass("Password: ")
    valid_credentials = True

    while not valid_credentials:
        user = input("Username: ")
        password = getpass("Password: ")
        valid_credentials = validateCredentials(user, password)

    option = input(
        "a.\tInsert\nb.\tDelete\nc.\tUpdate\nd.\tCreate Table\ne.\t Create view\nf.\tAlter\ng.\tQuery\nh.\tEXIT\nEnter letter to choose operation: ")

    valid_operation = validateOperation(option)

    while not valid_operation:
        option = input(
            "a.\tInsert\nb.\tDelete\nc.\tUpdate\nd.\tCreate Table\ne.\t Create view\nf.\tAlter\ng.\tQuery\nh.\tEXIT\nEnter letter to choose operation: ")
        valid_operation = validateOperation(option)

    if valid_operation == "a":
        tables = QueryBuilder(user, password, schema, 'country').getTableNames
        print(f"Tables in {schema}: {tables}")
        table_name = input("Table you want to insert data to:")

    if valid_operation == "b":
        table_name = input("Table to delete from: ")

    if valid_operation == "c":
        table_name = input("Table to update: ")

    if valid_operation == "d":
        table_name = input("Table name: ")
        num_attributes = int(input("Enter the number of attributes: "))
        i = 0
        while i < num_attributes:
            # ask for attribute name
            # data type

    if valid_operation == "e":
        table_name = input("Table ")

    if valid_operation == "f":
        table_name = input("Table ")

    if valid_operation == "g":
        table_name = input("Table ")

    if valid_operation == "h":
        exit()


if __name__ == "__main__":
    main()
