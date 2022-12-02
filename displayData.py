def displayTable(column_names, rows_list):
    longest_instance = {}
    for i in column_names:
        longest_instance[i] = len(i)

    for i in rows_list:
         for j in range(len(i)):
            if len(i[j]) > longest_instance[column_names[j]]:
                longest_instance[column_names[j]] = len(i[j])

    header_size = len(column_names)
    for i in range(header_size):
        print("{:<15s}".format(column_names[i]),end='')
    print()
    print(15*header_size*'-')
    for row in rows_list:
        for val in row:
            print("{:<15s}".format(str(val)),end='')
        print()
