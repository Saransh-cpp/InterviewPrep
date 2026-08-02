def smallestPalindrome(s):
    d = [0] * 26
    for c in s:
        d[ord(c) - 97] += 1
    res = ""
    flag = 0
    for i, freq in enumerate(d):
        res += (freq // 2) * chr(i + 97)
    for i, freq in enumerate(d):
        if freq & 1:
            res += chr(i + 97)
            flag = 1
    res = res + res[:-1][::-1] if flag else res + res[::-1]
    return res
