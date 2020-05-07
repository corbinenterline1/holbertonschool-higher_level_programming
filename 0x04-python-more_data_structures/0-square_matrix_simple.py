#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in range(len(matrix)):
            new_matrix.append(square_list(matrix[a]))
    return (new_matrix)


def square_list(list):
    return [i ** 2 for i in list]
