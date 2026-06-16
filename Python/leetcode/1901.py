def findPeakGrid(mat):
    low = 0
    high = len(mat[0]) - 1
    while low <= high:
        mid = (low + high) >> 1
        cols = [row[mid] for row in mat]
        peak = max(cols)
        row = cols.index(peak)
        left = mat[row][mid - 1] if mid > 0 else -1
        right = mat[row][mid + 1] if mid < high else -1
        if peak > left and peak > right:
            return [row, mid]
        elif peak < left:
            high = mid - 1
        else:
            low = mid + 1
