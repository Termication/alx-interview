#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
