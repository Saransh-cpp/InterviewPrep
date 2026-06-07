def generate(numRows):
    res = [[1], [1, 1]]
    if numRows == 1: return [res[0]]
    if numRows == 2: return res
    for i in range(3, numRows + 1):
        intm = [1]
        for j in range(len(res[i - 2]) - 1):
            intm.append(res[i - 2][j] + res[i - 2][j + 1])
        intm.append(1)
        res.append(intm)
    return res
