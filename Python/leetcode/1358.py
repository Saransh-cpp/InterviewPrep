def numberOfSubstrings(s):
    count = 0
    r = 0
    a = -1
    b = -1
    c = -1
    for r in range(len(s)):
        if s[r] == "a":
            a = r
        elif s[r] == "b":
            b = r
        else:
            c = r

        if a > -1 and b > -1 and c > -1:
            count += min(a, b, c) + 1

    return count

def numberOfSubstrings(s):
    count = 0
    r = 0
    freq = {"a": 0, "b": 0, "c": 0}
    while r < len(s):
        freq[s[r]] += 1
        temp_l = 0
        temp_freq = freq.copy()
        while all([x >= 1 for x in temp_freq.values()]):
            temp_freq[s[temp_l]] -= 1
            temp_l += 1
            count += 1
        r += 1
    return count
