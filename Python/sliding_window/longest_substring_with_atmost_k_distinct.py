def kDistinctChar(self, s, k):
    d = {}
    l = 0
    max_len = 0
    for r in range(len(s)):
        d[s[r]] = r
        if len(d) > k:
            del_idx = min(d.values())
            del d[s[del_idx]]
            l = del_idx + 1
        max_len = max(max_len, r - l + 1)
    return max_len
