def longestCommonPrefix(strs):
    strs.sort()
    res = ""
    for i, j in zip(strs[0], strs[-1]):
        if i != j: break
        res += i
    return res
