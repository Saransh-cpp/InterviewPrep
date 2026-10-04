def productExceptSelf(nums):
    prefix_prod = [1] * len(nums)
    suffix_prod = [1] * len(nums)
    running_prod = 1
    for i, n in enumerate(nums):
        prefix_prod[i] = running_prod
        running_prod *= n
    running_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        suffix_prod[i] = running_prod
        running_prod *= nums[i]
    res = []
    for n, m in zip(prefix_prod, suffix_prod):
        res += [n * m]

    return res
