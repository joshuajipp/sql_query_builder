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
            option_dict = {
                'a': "ADD",
                'b': "MODIFY",
                'c': "DROP"
            }
            data_type_dict = {
                'a': "VARCHAR(200)",
                'b': "INT(100)",
                'c': "CHAR(1)"
            }
            print(f"Tables in {schema}: {tables}")
            table_name = input("Table you want to alter: ")
            if validateTable(table_name, tables):
                obj = QueryBuilder(user, password, schema, table_name)
                column_info = obj.columnInfo()
                selection = input(
                    "\na.\tADD\nb.\tMODIFY\nc.\tDROP\nEnter a letter to choose which ALTER option to use: ")
                if selection.lower() in ['a', 'b', 'c']:
                    selection = option_dict[(selection.lower())]
                    if selection != "ADD":
                        print(
                            f"List of columns in {table_name}: {[x[0] for x in column_info]}")
                    column_name = input(
                        f"Enter the name of the column you want to {selection}: ")
                    if ((selection in ["MODIFY", "DROP"]) and (column_name in [x[0] for x in column_info])) or (not (selection in ["MODIFY", "DROP"]) and not (column_name in [x[0] for x in column_info])):
                        if selection in ["ADD", "MODIFY"]:
                            data_type = input(
                                f'\na.\tVARCHAR()\nb.\tINT()\nc.\tCHAR()\nEnter a letter to select data type for column "{column_name}": ')
                            if data_type.lower() in ['a', 'b', 'c']:
                                data_type = data_type_dict[data_type.lower()]
                                obj.addModify(
                                    selection, column_name, data_type)
                            else:
                                print("Invalid selection of data type.")
                        else:
                            obj.drop(column_name)
                    else:
                        if selection == "ADD":
                            print(
                                f'Column "{column_name}" is already in "{table_name}"')
                        else:
                            print(
                                f'Column "{column_name}" does not exist in "{table_name}"')

                else:
                    print("Invalid ALTER option.")

            else:
                print("Invalid table name.")

        if option == "g":
            table_name = input("Table ")
            """








        """

        if option == "h":
            print("Thankyou for using our SQL query writing program!")
            break


if __name__ == "__main__":
    main()
