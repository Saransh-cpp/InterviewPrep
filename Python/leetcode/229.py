def majorityElement(nums):
    count1 = 0
    count2 = 0
    el1 = 0
    el2 = 0
    for i in range(len(nums)):
        if count1 == 0 and nums[i] != el2:
            el1 = nums[i]
            count1 = 1
        elif count2 == 0 and nums[i] != el1:
            el2 = nums[i]
            count2 = 1
        elif nums[i] == el1:
            count1 += 1
        elif nums[i] == el2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    res = []
    count1 = 0
    count2 = 0
    for num in nums:
        if num == el1: count1 += 1
        elif num == el2: count2 += 1

    threshold = len(nums) // 3
    if count1 > threshold: res.append(el1)
    if count2 > threshold: res.append(el2)

    return res
