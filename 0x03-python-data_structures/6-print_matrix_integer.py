#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l1 = len(matrix)
    if not matrix[0]:
        print()
        for t in range(l1):
            l2 = len(matrix[t])
            for c in range(l2):
                if c == l2 - 1:
                    print("{:d}".format(matrix[t][c]))
                else:
                    print("{:d}".format(matrix[t][c]), end="")
