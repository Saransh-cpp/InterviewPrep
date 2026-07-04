def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    greed = 0
    size = 0
    while greed < len(g) and size < len(s):
        if g[greed] <= s[size]:
            count += 1
            greed += 1
            size += 1
        else:
            size += 1
    return count
