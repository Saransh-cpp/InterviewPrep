# def removeDuplicates(nums):
#     j = 0

#     for i in range(1, len(nums)):
#         if nums[i] != nums[j]:
#             j += 1
#             nums[j] = nums[i]
    
#     return j + 1


def removeDuplicates(nums):
    j = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            j += 1
            nums[j] = nums[i]
    
    return j + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    arg_nums = nums.copy()
    k = removeDuplicates(arg_nums)
    print(nums, arg_nums[:k])

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arg_nums = nums.copy()
    k = removeDuplicates(arg_nums)
    print(nums, arg_nums[:k])
