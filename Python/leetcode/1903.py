def largestOddNumber(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) & 1:
            return num[0:i+1]
    return ""
