#!/usr/bin/python3


'''Describes a Pascal's Triangle func'''


def pascal_triangle(k):
    '''Represent a pascal's triangle of size k
    Returns list of lists of integers representing the tri'''
    if k <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != k:
        tri = triangles[-1]
        tmp = [1]
        for n in range(len(tri) - 1):
            tmp.append(tri[n] + tri[n + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
