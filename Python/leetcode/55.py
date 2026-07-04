def canJump(nums):
    maxx = 0
    for i in range(len(nums)):
        if i > maxx:
            return False
        maxx = max(maxx, i + nums[i])
    return True
