def singleNumber(nums):
    nums = sorted(nums)
    for i in range(1, len(nums), 3):
        if nums[i] != nums[i - 1]:
            return nums[i - 1]
    return nums[-1]

def singleNumber(nums):
    ans = 0
    for i in range(32):
        set_bits = 0
        for num in nums:
            if num < 0:
                num = num & (2**32-1)
            if num & (1 << i) != 0:
                set_bits += 1
        if set_bits % 3 == 1:
            ans |= 1 << i
    if ans >= 2**31:
        ans -= 2**32
    return ans
