def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    brk = None
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            brk = i - 1
            break
    if brk is None:
        nums.sort()
    else:
        for i in range(len(nums) - 1, brk, -1):
            if nums[i] > nums[brk]:
                nums[brk], nums[i] = nums[i], nums[brk]
                break
        # temp = nums[brk + 1:]
        # temp.sort()
        # nums[brk + 1:] = temp
        nums[brk + 1:] = nums[brk + 1:][::-1]
