def reverseWords(s):
    s = s.strip()
    s = s[::-1]
    fast = 0
    slow = 0
    res = ""
    while fast < len(s):
        if s[fast] == " ":
            res += s[slow:fast][::-1]
            res += " "
            while fast < len(s) and s[fast] == " ":
                fast += 1
            slow = fast
        else:
            fast += 1
    res += s[slow:fast][::-1]
    return res
