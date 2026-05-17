def check(nums):
    breaks = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i]:
            breaks += 1
    if nums[-1] > nums[0]:
        breaks +=1

    return breaks == 0 or breaks == 1
