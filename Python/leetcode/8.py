def myAtoi(s):
    res = 0
    s = s.strip()
    if s == "": return 0

    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]

    for c in s:
        if ord(c) == 48 and res == 0: continue

        if ord(c) >= 48 and ord(c) <= 57:
            res = (res * 10) + (ord(c) - 48)
            if sign * res >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif sign * res <= - 2 ** 31:
                return - 2 ** 31
        else:
            break
    return sign * res
