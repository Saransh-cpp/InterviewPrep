# def removeElement(nums, val):
#     if nums == []: return 0
#     if all(i == val for i in nums): return 0

#     j = len(nums) - 1
#     while (nums[j] == val):
#         j -= 1
    
#     for i in range(j - 1, -1, -1):
#         if nums[i] == val:
#             nums[i], nums[j] = nums[j], nums[i]
#             j -=1
    
#     return j + 1


def removeElement(nums, val):
    j = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    
    return j


if __name__ == "__main__":
    nums = [3, 2 , 2, 3]
    val = 3
    arg_nums = nums.copy()
    k = removeElement(arg_nums, val)
    print(nums, arg_nums[:k])

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    arg_nums = nums.copy()
    k = removeElement(arg_nums, val)
    print(nums, arg_nums[:k])
