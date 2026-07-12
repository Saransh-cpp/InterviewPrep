def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    summ = candies[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        summ += candies[i]

    return summ

def candy(ratings):
    i = 1
    summ = 1
    n = len(ratings)
    while i < n:
        if i < n and ratings[i] == ratings[i - 1]:
            summ += 1
            i += 1
            continue
        peak = 1
        while i < n and ratings[i] > ratings[i - 1]:
            peak += 1
            summ += peak
            i += 1
        trough = 1
        while i < n and ratings[i] < ratings[i - 1]:
            summ += trough
            i += 1
            trough += 1
        if trough > peak:
            summ += (trough - peak)
    return summ
