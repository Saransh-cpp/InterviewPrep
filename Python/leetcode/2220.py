def minBitFlips(start, goal):
    flips = start ^ goal
    res = 0
    while (flips > 1):
        # if (n % 2 == 1): rest += 1
        res += flips & 1
        flips = flips >> 1
    return res + 1 if flips == 1 else res
