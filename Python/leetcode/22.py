def generateParenthesis(n):
    res = []
    recurse(0, "", res, 0, 0, n)
    return res

def recurse(ind, s, res, openings, closings, n):
    if openings > n:
        return
    if openings == closings == n:
        res += [s]
        return
    recurse(ind + 1, s + "(", res, openings + 1, closings, n)
    if closings < openings:
        recurse(ind + 1, s + ")", res, openings, closings + 1, n)
