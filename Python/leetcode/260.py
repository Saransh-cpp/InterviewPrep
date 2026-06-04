def singleNumber(nums):
    xord = 0
    for num in nums:
        xord ^= num
    mask = (xord & (xord - 1)) ^ xord
    b1 = 0
    b2 = 0
    for num in nums:
        if num & mask != 0:
            b1 ^= num
        else:
            b2 ^= num
    return [b1, b2]
