def searchMatrix(matrix, target):
    low = 0
    n = len(matrix)
    m = len(matrix[0])
    high = (n * m) - 1

    while low <= high:
        mid = (low + high) >> 1

        i = mid // m
        j = mid % m
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
