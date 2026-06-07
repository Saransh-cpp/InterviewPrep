def spiralOrder(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows == 1: return matrix[0]

    res = []
    i, j = 0, 0
    while matrix[i][j] is not None:
        while j < cols:
            res.append(matrix[i][j])
            matrix[i][j] = None
            if j < cols - 1 and matrix[i][j + 1] is not None:
                j += 1
            else:
                break
        i += 1
        if matrix[i][j] is None:
            break
        while i < rows:
            res.append(matrix[i][j])
            matrix[i][j] = None
            if i < rows - 1 and matrix[i + 1][j] is not None:
                i += 1
            else:
                break
        j -= 1
        if matrix[i][j] is None:
            break
        while j > -1:
            res.append(matrix[i][j])
            matrix[i][j] = None
            if j > 0 and matrix[i][j - 1] is not None:
                j -= 1
            else:
                break
        i -= 1
        if matrix[i][j] is None:
            break
        while i > -1:
            res.append(matrix[i][j])
            matrix[i][j] = None
            if i > 0 and matrix[i - 1][j] is not None:
                i -= 1
            else:
                break
        j += 1
    return res


def spiralOrder(matrix):
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    top = 0
    left = 0

    res = []
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res
