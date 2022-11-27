import mysql.connector
from queryClass import *
from validate import *
from getpass import getpass


def main():
    schema = "olympicarchery"
    user = input("Username: ")
    password = getpass("Password: ")
    valid_credentials = validateCredentials(user, password)

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

    if option == "a":
        tables = QueryBuilder(user, password, schema, 'country').getTableNames()
        print(f"Tables in {schema}: {tables}")
        table_name = input("Table you want to insert data to: ")
        obj = QueryBuilder(user, password, schema, table_name)
        column_info = obj.columnInfo()
        print(column_info)
    
    
    
    
    
    
    
    if option == "b":
        table_name = input("Table to delete from: ")
        valid_tablename = validateTable(table_name)
        condition = input("Please enter the condition (for example: The condition is the Olympic ID number from the athlete table): ")
        #valid_condition  = validateCondition(condition)
        valid_condition = True
            


    
    
    
    
    
    
    if option == "c":
        table_name = input("Table to update: ")
        """
    
    
    
    
    
    
    
    
    """
    if option == "d":
        table_name = input("Table name: ")
        num_attributes = int(input("Enter the number of attributes: "))
        i = 0
        #while i < num_attributes:
            # ask for attribute name
            # data type
    
    
    
    
    
    
    
    
    
        
    if option == "e":
        table_name = input("Table ")
    """
    
    
    
    
    
    
    
    
    """
    if option == "f":
        table_name = input("Table ")
        """
    
    
    
    
    
    
    
    
    """

    if option == "g":
        table_name = input("Table ")
        """








    """

    if option == "h":
        exit()


if __name__ == "__main__":
    main()