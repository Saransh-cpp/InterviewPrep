def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    new_m = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_m[j][len(matrix[0]) - 1 - i] = matrix[i][j]
    matrix[:] = new_m[:]


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
