def minWindow(s, t):
    l = 0
    minlen = float("inf")
    count = 0
    ind = -1
    key_freq, win_freq = {}, {}
    for c in t:
        key_freq[c] = key_freq.get(c, 0) + 1

    for r in range(len(s)):
        win_freq[s[r]] = win_freq.get(s[r], 0) + 1
        if s[r] in key_freq and key_freq[s[r]] == win_freq[s[r]]:
            count += 1
        while count == len(key_freq):
            if r - l + 1 < minlen:
                ind = l
                minlen = r - l + 1
            win_freq[s[l]] -= 1
            if s[l] in key_freq and win_freq[s[l]] < key_freq[s[l]]:
                count -= 1
            l += 1

    return "" if ind == -1 else s[ind:ind+minlen]
