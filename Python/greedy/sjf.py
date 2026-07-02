def solve(bt):
    bt.sort()
    wt = 0
    t = 0
    for b in bt:
        wt += t
        t += b
    return wt // len(bt)
