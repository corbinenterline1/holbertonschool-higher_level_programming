#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0]:
        for a in range(len(matrix)):
            for b in range(len(matrix[a])):
                if b + 1 == len(matrix[a]):
                    print("{:d}".format(matrix[a][b]))
                else:
                    print("{:d}".format(matrix[a][b]), end=' ')
    else:
        print()
