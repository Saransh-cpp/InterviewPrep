def largestAltitude(gain):
    res = 0
    summ = 0
    for num in gain:
        summ += num
        res = max(summ, res)
    return res
