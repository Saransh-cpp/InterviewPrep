def shipWithinDays(weights, days):
    low = max(weights)
    high = sum(weights)

    while low <= high:
        mid = (low + high) >> 1
        day = 1
        curr_weight = 0
        for w in weights:
            if curr_weight + w > mid:
                day += 1
                curr_weight = w
            else:
                curr_weight += w

        if day <= days:
            high = mid - 1
        else:
            low = mid + 1
    return low
