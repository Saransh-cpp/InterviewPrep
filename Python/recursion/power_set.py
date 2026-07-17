def powerSet(nums):
    res = []
    recurse(0, [], res, nums)
    return res

def recurse(ind, lst, res, nums):
    if len(nums) == ind:
        res += [lst]
        return
    recurse(ind + 1, lst + [nums[ind]], res, nums)
    recurse(ind + 1, lst, res, nums)


if __name__ == "__main__":
    nums = [1, 2]
    print(powerSet(nums))
