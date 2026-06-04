def hammingWeight(n):
    count = 1
    while (n > 1):
        count += n & 1
        n = n >> 1
    return count

def hammingWeight(n):
    count = 0
    while (n > 0):
        n &= (n - 1)
        count += 1
    return count
