def lengthOfLongestSubstring(s):
    max_len = 0
    i = 0
    j = 0
    count = 0
    d = {}
    while i < len(s):
        if s[i] not in d:
            d[s[i]] = i
            count += 1
            max_len = max(max_len, count)
        else:
            ind = d[s[i]] + 1
            while j != ind:
                del d[s[j]]
                j += 1
            count = i - j + 1
            d[s[i]] = i
        i += 1
    return max_len
