def maxScore(cardPoints, k):
    left_sum = 0
    for point in cardPoints[:k]:
        left_sum += point
    right_sum = 0
    summ = left_sum + right_sum
    l = len(cardPoints) - 1
    r = k - 1
    while r > -1:
        left_sum -= cardPoints[r]
        r -= 1
        right_sum += cardPoints[l]
        l -= 1
        summ = max(summ, left_sum + right_sum)
    return summ
