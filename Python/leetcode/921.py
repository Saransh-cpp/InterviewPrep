from collections import deque


def minAddToMakeValid(s):
    store = deque()
    for c in s:
        if c == "(":
            store.append(c)
        else:
            if len(store) != 0 and store[-1] == "(":
                store.pop()
            else:
                store.append(c)
    return len(store)

def minAddToMakeValid(s):
    open_brackets = 0
    res = 0
    for c in s:
        if c == "(":
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
            else:
                res += 1

    return res + open_brackets
