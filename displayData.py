def displayTable(column_names, rows_list):
    longest_instance = {}
    for i in column_names:
        longest_instance[i] = len(i)

    for i in rows_list:
        for j in range(len(i)):
            if len(i[j]) > longest_instance[column_names[j]]:
                longest_instance[column_names[j]] = len(i[j])
