def combinationSum3(k, n):
    res = []
    recurse([], k, n, res, n)
    return res

def recurse(curr, k, n, res, summ):
    if summ == 0 and len(curr) == k:
        res += [curr]
        return
    elif summ < 0 or len(curr) > k:
        return
    el = 1 if not curr else curr[-1] + 1
    for i in range(el, 10):
        recurse(curr + [i], k, n, res, summ - i)
