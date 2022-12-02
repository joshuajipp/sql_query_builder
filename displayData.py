def displayTable(column_names, rows_list):
    
    header_size = len(column_names)
    for i in range(header_size):
        print("{:<15s}".format(column_names[i]),end='')
    print()
    print(15*header_size*'-')
    for row in rows_list:
        for val in row:
            print("{:<15s}".format(str(val)),end='')
        print()
