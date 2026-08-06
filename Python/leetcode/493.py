class Solution:
    def __init__(self):
        self.count = 0

    def reversePairs(self, nums):
        self.recurse(nums, 0, len(nums) - 1)
        return self.count

    def count_pairs(self, nums, low, mid, high):
        j = mid + 1
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            self.count += j - mid - 1

    def recurse(self, nums, low, high):
        if low >= high:
            return
        mid = (low + high) >> 1
        self.recurse(nums, low, mid)
        self.recurse(nums, mid + 1, high)
        self.count_pairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        i = low
        j = mid + 1
        merged = []
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                merged += [nums[i]]
                i += 1
            else:
                merged += [nums[j]]
                j += 1
        while i <= mid:
            merged += [nums[i]]
            i += 1
        while j <= high:
            merged += [nums[j]]
            j += 1
        for i in range(low, high + 1):
            nums[i] = merged[i - low]
