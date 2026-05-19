def fourSum(nums, target: int):
    nums = sorted(nums)
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]: continue
        j = i + 1
        while j < len(nums):
            front = j + 1
            back = len(nums) - 1
            while front < back:
                if nums[i] + nums[j] + nums[front] + nums[back] > target:
                    back -= 1
                elif nums[i] + nums[j] + nums[front] + nums[back] < target:
                    front += 1
                else:
                    res.append([nums[i], nums[j], nums[front], nums[back]])
                    front += 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1
                    # can add
                    # back -= 1
                    # while front < back and nums[back] == nums[back + 1]:
                    #     back -= 1
            j += 1
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1
    return res
