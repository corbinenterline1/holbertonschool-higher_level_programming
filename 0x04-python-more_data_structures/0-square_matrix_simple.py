#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in range(len(matrix)):
            new_matrix.append([i ** 2 for i in matrix[a]])
    return (new_matrix)
