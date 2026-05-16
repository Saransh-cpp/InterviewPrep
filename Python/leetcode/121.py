def maxProfit(prices):
    min_el = prices[0]
    maxp = 0
    for i in range(len(prices)):
        if prices[i] < min_el:
            min_el = prices[i]
        currp = prices[i] - min_el
        if currp > maxp:
            maxp = currp
    return maxp
