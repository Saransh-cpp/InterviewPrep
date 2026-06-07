def findErrorNums(nums):
    nums.sort()
    repeated = 0
    missing = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            repeated = nums[i]
            break

    arr_summ = sum(nums) - repeated
    summ = (len(nums) * (len(nums) + 1)) / 2
    missing = summ - arr_summ
    return [repeated, int(missing)]


def findErrorNums(nums):
    xord = 0
    for num in nums:
        xord ^= num
    for i in range(len(nums) + 1):
        xord ^= i
    
    mask = xord & ~(xord - 1)

    b1 = 0
    b2 = 0
    for num in nums:
        if num & mask != 0: b1 ^= num
        else: b2 ^= num
    for i in range(len(nums) + 1):
        if i & mask != 0: b1 ^= i
        else: b2 ^= i

    count_b1 = 0
    count_b2 = 0
    for num in nums:
        if num == b1: count_b1 += 1
        elif num == b2: count_b2 += 1

    repeated = b1 if count_b1 == 2 else b2
    missing = b2 if repeated == b1 else b1

    return [repeated, missing]
