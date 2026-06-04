def subsets(nums):
    res = []
    for i in range(1 << len(nums)):
        subres = []
        for bit in range(len(nums)):
            if i & 1 << bit != 0:
                subres.append(nums[bit])
        res.append(subres)
    return res
