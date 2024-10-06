#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n
    """
    if n <= 0:
        return []

    triangle = [0] * n

    for i in range(n):
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = triangle[i - 1][j]
                b = triangle[i - 1][j - 1]
                new_row[j] = a + b

        triangle[i] = new_row

    return triangle
