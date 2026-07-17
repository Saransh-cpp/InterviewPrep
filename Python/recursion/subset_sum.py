def subsetSums(nums):
    res = []
    recurse(0, res, nums, 0)
    return res

def recurse(ind, res, nums, summ):
    if ind == len(nums):
        res += [summ]
        return
    recurse(ind + 1, res, nums, summ + nums[ind])
    recurse(ind + 1, res, nums, summ)
