#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new_line = ""
    for row in matrix:
        length = len(row)
        for i in range(length):
            if i != length - 1:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]), end='')
        print("{}".format(new_line))
