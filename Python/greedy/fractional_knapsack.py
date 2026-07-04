def fractionalKnapsack(self, val, wt, cap):
    arr = [(i, j) for i, j in zip(val, wt)]
    arr.sort(key=lambda x : -(x[0] / x[1]))
    res = 0
    for a in arr:
        if a[1] > cap:
            res +=  (cap / a[1]) * a[0]
            break
        res += a[0]
        cap -= a[1]
    return res      
