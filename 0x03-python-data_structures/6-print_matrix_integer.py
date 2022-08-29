#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for intg in range(len(row)):
            print("{:d}".format(row[intg]), end="" if intg == len(row) - 1 else " ")
        print("")
