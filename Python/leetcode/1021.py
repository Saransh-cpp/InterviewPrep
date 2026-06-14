def removeOuterParentheses(s):
    res = ""
    count = 0
    slow = 0
    fast = 0
    while fast < len(s):
        if s[fast] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            res += s[slow + 1: fast]
            slow = fast + 1
            count = 0
        fast += 1
    return res
