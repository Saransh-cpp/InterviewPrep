class Solution:
    def __init__(self):
        self.count = 0

    def countSubsequenceWithTargetSum(self, nums, k):
        self.recurse(0, [], nums, k)
        return self.count

    def recurse(self, ind, curr, nums, k):
        if ind == len(nums):
            if sum(curr) == k:
                self.count += 1
            return
        self.recurse(ind + 1, curr + [nums[ind]], nums, k)
        self.recurse(ind + 1, curr, nums, k)


class Solution:
    def __init__(self):
        self.count = 0

    def countSubsequenceWithTargetSum(self, nums, k):
        self.recurse(0, [], nums, k, 0)
        return self.count

    def recurse(self, ind, curr, nums, k, summ):
        if ind == len(nums):
            if summ == k:
                self.count += 1
            return
        self.recurse(ind + 1, curr + [nums[ind]], nums, k, summ + nums[ind])
        self.recurse(ind + 1, curr, nums, k, summ)


class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        return self.recurse(0, [], nums, k, 0)

    def recurse(self, ind, curr, nums, k, summ):
        if ind == len(nums):
            if summ == k:
                return 1
            else:
                return 0
        l = self.recurse(ind + 1, curr + [nums[ind]], nums, k, summ + nums[ind])
        r = self.recurse(ind + 1, curr, nums, k, summ)
        return l + r
