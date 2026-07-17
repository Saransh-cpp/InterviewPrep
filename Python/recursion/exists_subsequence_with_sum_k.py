class Solution:
    def checkSubsequenceSum(self, nums, k):
        return self.recurse(0, [], nums, k)

    def recurse(self, ind, curr, nums, k):
        if ind == len(nums):
            if sum(curr) == k:
                return True
            return
        res = self.recurse(ind + 1, curr + [nums[ind]], nums, k)
        if res:
            return True
        res1 = self.recurse(ind + 1, curr, nums, k)
        if res1:
            return True
        return False


class Solution:
    def checkSubsequenceSum(self, nums, k):
        return self.recurse(0, [], nums, k, 0)

    def recurse(self, ind, curr, nums, k, summ):
        if ind == len(nums):
            if summ == k:
                return True
            else:
                return False
        if self.recurse(ind + 1, curr + [nums[ind]], nums, k, summ + nums[ind]):
            return True
        if self.recurse(ind + 1, curr, nums, k, summ):
            return True
        return False
