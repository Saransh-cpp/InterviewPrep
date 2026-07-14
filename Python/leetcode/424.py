def characterReplacement(s, k):
    d = {}
    l = 0
    r = 0
    maxlen = 0
    while r < len(s):
        d[s[r]] = d.get(s[r], 0) + 1
        if r - l + 1 - max(d.values()) > k:
            d[s[l]] -= 1
            l += 1
        maxlen = max(maxlen, r - l + 1)
        r += 1
    return maxlen
