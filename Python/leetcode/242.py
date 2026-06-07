def isAnagram(s, t):
    if len(s) != len(t): return False

    d1 = [0] * 26
    for i in range(len(s)):
        d1[ord(s[i]) - ord('a')] += 1
        d1[ord(t[i]) - ord('a')] -= 1

    for v in d1:
        if v != 0: return False

    return True
