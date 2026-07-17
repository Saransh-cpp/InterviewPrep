def subsetsWithDup(nums):
    res = []
    nums.sort()
    recurse(0, [], res, nums)
    return res

def recurse(ind, curr, res, nums):
    if ind == len(nums):
        res += [curr]
        return
    recurse(ind + 1, curr + [nums[ind]], res, nums)
    for i in range(ind + 1, len(nums)):
        if nums[i] != nums[ind]:
            recurse(i, curr, res, nums)
            return
    recurse(len(nums), curr, res, nums)
