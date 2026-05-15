def twoSum(nums, target):
    d = {}

    for i in range(len(nums)):
        if target - nums[i] in d:
            return [i, d[target - nums[i]]]
        d[nums[i]] = i


# def twoSum(nums, target):
#     nums = sorted(nums)

#     j = len(nums) - 1
#     i = 0
#     while i < len(nums) - 1:
#         if nums[i] + nums[j] > target:
#             j -= 1
#         elif nums[i] + nums[j] < target:
#             i += 1
#         else:
#             return True


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    indices = twoSum(nums, target)
    print(indices)

    nums = [3, 2, 4]
    target = 6
    indices = twoSum(nums, target)
    print(indices)

    nums = [3, 3]
    target = 6
    indices = twoSum(nums, target)
    print(indices)
