def totalFruit(fruits):
    d = {}
    l = 0
    r = 0
    length = 0
    max_len = 0
    while r < len(fruits):
        if fruits[r] in d:
            d[fruits[r]] = r
            length += 1
            max_len = max(max_len, length)
        else:
            if len(d) == 2:
                l = min(d.values()) + 1
                length = r - l + 1
                del d[min(d, key=d.get)]
                d[fruits[l]] = r - 1
                d[fruits[r]] = r
            else:
                d[fruits[r]] = r
                length += 1
                max_len = max(max_len, length)
        r += 1
    return max_len
