#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for line in matrix:
        squares.append([ele**2 for ele in line])
    return squares
