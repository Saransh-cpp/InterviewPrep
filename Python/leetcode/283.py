def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    for j in range(i, len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] != 0:
            i += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)

    nums = [1, 2, 0, 1, 0, 4, 0]
    moveZeroes(nums)
    print(nums)

    nums = [1, 0, 2, 3, 0, 4, 0, 1]
    moveZeroes(nums)
    print(nums)
