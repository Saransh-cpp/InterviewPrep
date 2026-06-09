def minDays(bloomDay, m, k):
    low = 1
    high = max(bloomDay)

    if m * k > len(bloomDay):
        return -1

    while low <= high:
        mid = (low + high) >> 1
        bq = 0
        fl = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                fl += 1
                if fl == k:
                    bq += 1
                    fl = 0
            else:
                fl = 0
        if bq >= m:
            high = mid - 1
        else:
            low = mid + 1
    return low
