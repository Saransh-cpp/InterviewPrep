def searchMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while (col >= 0 and row < len(matrix)):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False
