def maxDistance(position, m):
    position.sort()
    low = 1
    high = position[-1] - position[0]
    while low <= high:
        mid = (low + high) >> 1
        balls = 1
        last = position[0]
        for p in position[1:]:
            if p - last >= mid:
                balls += 1
                last = p
        if balls < m:
            high = mid - 1
        else:
            low = mid + 1
    return high
