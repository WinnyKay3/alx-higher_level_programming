#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    for t in range(len(matrix)):
        k = len(matrix[t])
        for c in range(k):
            e = "\n" if c is (k - 1) else " "
            print("{:d}".format(matrix[t][c]), end=e)
