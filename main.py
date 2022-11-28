import mysql.connector
from queryClass import *
from validate import *
from getpass import getpass


def main():

    user = input("Username: ")
    password = getpass("Password: ")
    valid_credentials = validateCredentials(user, password)
    while not valid_credentials:
        user = input("Username: ")
        password = getpass("Password: ")
        valid_credentials = validateCredentials(user, password)

    schema = "olympicarchery"
    tables = QueryBuilder(user, password, schema,
                          'participant').getTableNames()
    datatype_dict = {
        253: "Enter an alphanumeric string value: ",
        254: "Enter a character value (e.g. M for male and F for female): ",
        3: "Enter an integer value: "
    }
    while True:
        option = input(
            "\na.\tInsert\nb.\tDelete\nc.\tUpdate\nd.\tCreate Table\ne.\t Create view\nf.\tAlter\ng.\tQuery\nh.\tEXIT\nEnter letter to choose operation: ")

        valid_operation = validateOperation(option)

        while not valid_operation:
            print("Invalid option. Please try again.")
            option = input(
                "\na.\tInsert\nb.\tDelete\nc.\tUpdate\nd.\tCreate Table\ne.\t Create view\nf.\tAlter\ng.\tQuery\nh.\tEXIT\nEnter letter to choose operation: ")
            valid_operation = validateOperation(option)

        if option == "a":
            print(f"Tables in {schema}: {tables}")
            table_name = input("Table you want to insert data to: ")
            if validateTable(table_name, tables):
                obj = QueryBuilder(user, password, schema, table_name)
                column_info = obj.columnInfo()
                for i in column_info:
                    print(f'\nInserting into column "{i[0]}"...')
                    col_inp = input(f"{datatype_dict[i[1]]}")

                    if validateColumnInput(col_inp, i) != True:
                        print(validateColumnInput(col_inp, i))
                        break
            else:
                print("Invalid table name.")

        if option == "b":
            table_name = input("Table to delete from: ")
            valid_tablename = validateTable(table_name)
            condition = input(
                "Please enter the condition (for example: The condition is the Olympic ID number from the athlete table): ")
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
            # while i < num_attributes:
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
            print("Thankyou for using our SQL query writing program!")
            break


if __name__ == "__main__":
    main()
