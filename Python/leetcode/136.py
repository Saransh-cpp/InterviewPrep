def singleNumber(nums):
    xord = 0
    for n in nums:
        xord ^= n
    
    return xord
