from math import ceil


def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)

    while low <= high:
        mid = (low + high) >> 1
        t = 0
        for pile in piles:
            t += ceil(pile / mid)
        if t > h:
            low = mid + 1
        else:
            high = mid - 1

    return low
