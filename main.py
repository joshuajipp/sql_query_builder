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
        option = option.lower()
        if option == "a":
            print(f"Tables in {schema}: {tables}")
            table_name = input("Table you want to insert data to: ")
            if validateTable(table_name, tables):
                obj = QueryBuilder(user, password, schema, table_name)
                column_info = obj.columnInfo()
                insert_info = []
                for i in column_info:
                    if i[2] == 0:
                        print("\n**REQUIRED FIELD**")
                    print(f'Inserting into column "{i[0]}"...')
                    col_inp = input(f"{datatype_dict[i[1]]}")

                    if validateColumnInput(col_inp, i) != True:
                        print(validateColumnInput(col_inp, i))
                        break
                    if col_inp == '':
                        col_inp = None
                    insert_info.append(col_inp)
                obj.insert(tuple(insert_info))
            else:
                print("Invalid table name.")

        if option == "b":
            print(f"Tables in {schema}: {tables}")
            table_name = input("Enter table to delete from: ")
            if validateTable(table_name, tables):
                obj = QueryBuilder(user, password, schema, table_name)
                column_info = obj.columnInfo()
                print(
                    f"\nList of columns in {table_name}: {[x[0] for x in column_info]}")
                condition = input(
                    "Enter a WHERE condition in the form: ColumnName = 'Column Value'\n")
                if (condition.split(' '))[0] in [x[0] for x in column_info]:

                    obj.delete(condition)
                else:
                    print(
                        f"{condition.split(' ')[0]} is not a valid column in {table_name}")

            else:
                print("Invalid table name.")

        if option == "c":
            print(f"Tables in {schema}: {tables}")
            table_name = input("Enter table to update: ")
            if validateTable(table_name, tables):
                obj = QueryBuilder(user, password, schema, table_name)
                column_info = obj.columnInfo()
                set_list = []

                for i in column_info:
                    toggle = input(
                        f'\nEnter "Y" to set value of column "{i[0]}", or enter anything else to skip: ')
                    if toggle.lower() == 'y':
                        tmp_str = ""
                        if i[2] == 0:
                            print("\n**REQUIRED FIELD**")
                        print(f'Updating values in column "{i[0]}"...')
                        col_inp = input(f"{datatype_dict[i[1]]}")

                        if validateColumnInput(col_inp, i) != True:
                            print(validateColumnInput(col_inp, i))
                            break

                        if col_inp != "":
                            tmp_str = f"{i[0]} = '{col_inp}'"
                        else:
                            tmp_str = f"{i[0]} = NULL"
                        set_list.append(tmp_str)

                print(
                    f"\nList of columns in {table_name}: {[x[0] for x in column_info]}")
                condition = input(
                    "Enter a WHERE condition in the form: ColumnName = 'Column Value'\n")
                if (condition.split(' '))[0] in [x[0] for x in column_info]:
                    set_list = ", ".join(set_list)
                    obj.update(set_list, condition)
                    print(set_list)
                    print(condition)
                else:
                    print(
                        f"{condition.split(' ')[0]} is not a valid column in {table_name}")

            else:
                print("Invalid table name.")

        if option == "d":
            table_name = input(
                "Enter the name of the table you want to create: ")
            col_lst = []
            if not (table_name in tables):
                col_name = input("Enter column name: ")
                data_type = input(
                    f'\na.\tVARCHAR()\nb.\tINT()\nc.\tCHAR()\nEnter a letter to select data type for column "{col_name}": ')
                if data_type.lower() in ['a', 'b', 'c']:
                    data_type = data_type_dict[data_type.lower()]
                    col_lst.append(f"{col_name} {data_type}")
                while True:
                    dec = input(
                        'Enter "Y" to add another column, else enter any other value: ')
                    if not (dec.lower() == "y"):
                        break
                    col_name = input("Enter column name: ")
                    data_type = input(
                        f'\na.\tVARCHAR()\nb.\tINT()\nc.\tCHAR()\nEnter a letter to select data type for column "{col_name}": ')
                    if data_type.lower() in ['a', 'b', 'c']:
                        data_type = data_type_dict[data_type.lower()]
                        col_lst.append(f"{col_name} {data_type}")

                    else:
                        print("Invalid selection of data type.")

            else:
                print(f'Table {table_name} already exists in the database')

        if option == "e":
            table_name = input(
                "Enter the name of the view you want to create: ")
            if not (table_name in tables):
                pass
            else:
                print(f'View {table_name} already exists in the database')

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
            print(f"Tables in {schema}: {tables}")
            table_name = input("Enter the table you would like to query: ")
            if validateTable(table_name, tables):
                obj = QueryBuilder(user, password, schema, table_name)
                column_info = obj.columnInfo()
                cols = [x[0] for x in column_info]
                print(
                    f"\nList of columns in {table_name}: {cols}")
                sel_columns = input(
                    'Enter * to select all columns or specify each column separated by spaces: ')
                sel_columns = sel_columns.split(" ")
                if sel_columns[0] == '*':
                    sel_columns = cols
                act_list = []
                for i in sel_columns:
                    if i in cols:
                        act_list.append(i)
                if len(act_list) == len(sel_columns):
                    where_dec = input(
                        'Enter "Y" to add a WHERE condition, enter anything else to skip: ')
                    condition = None
                    if where_dec.lower() == 'y':
                        condition = input(
                            "Enter a WHERE condition in the form: ColumnName = 'Column Value'\n")

                    if (condition == None) or ((condition.split(' '))[0] in cols):
                        order_dec = input(
                            'Enter "Y" to ORDER BY a particular column, enter anything else to skip: ')
                        order_col = None
                        not_in = []
                        if order_dec.lower() == 'y':
                            order_col = input(
                                "Enter an individual column or list of columns separated by spaces for which you want to order your table by: ")
                            order_col = order_col.split(' ')
                            for i in order_col:
                                if not (i in cols):
                                    not_in.append(i)
                        if len(not_in) == 0:
                            sel_columns = ", ".join(sel_columns)
                            if order_col != None:
                                order_col = ", ".join(order_col)
                            print(obj.query(sel_columns,
                                            condition, order_col))
                        else:
                            print(f"Columns {not_in} are not in {table_name}")

                    else:
                        print(
                            f"{condition.split(' ')[0]} is not a valid column in {table_name}")

                    # order_dec = input(
                    #     'Enter "Y" to ORDER BY a particular column, enter anything else to skip: ')
                    # if order_dec.lower() == 'y':
                    #     order_col = input(
                    #         "Enter an individual column or list of columns separated by spaces for which you want to order your table by: ")
                    #     order_col = order_col.split(' ')
                    #     not_in = []
                    #     for i in order_col:
                    #         if not (i in cols):
                    #             not_in.append(i)
                    #     if len(not_in) == 0:
                    #         obj.query(sel_columns, condition, order_col)
                    #     else:
                    #         print(f"Columns {not_in} are not in {table_name}")

                    #     if not (condition.split(' '))[0] in [x[0] for x in column_info]:
                    #         print(
                    #             f"{condition.split(' ')[0]} is not a valid column in {table_name}")
                    #         break
                    # else:
                    #     condition = None

                else:
                    print(
                        f"Column(s) {[x for x in sel_columns if not(x in act_list)]} are not in table {table_name}")

            else:
                print("Invalid table name.")

        if option == "h":
            print("Thankyou for using our SQL query writing program!")
            break


if __name__ == "__main__":
    main()
