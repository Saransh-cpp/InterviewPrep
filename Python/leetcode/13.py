def romanToInt(s):
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    res = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and mapping[s[i]] < mapping[s[i + 1]]:
            res += mapping[s[i + 1]] - mapping[s[i]]
            i += 1
        else:
            res += mapping[s[i]]
        i += 1
    return res
