def threeSum(nums):
    res = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]: continue
        front = i + 1
        back = len(nums) - 1
        while front < back:
            if nums[front] + nums[back] + nums[i] > 0:
                back -= 1
            elif nums[front] + nums[back] + nums[i] < 0:
                front += 1
            else:
                res.append([nums[front], nums[back], nums[i]])
                front += 1
                while nums[front] == nums[front - 1] and front < back:
                    front += 1
                # can add
                # back -= 1
                # while front < back and nums[back] == nums[back + 1]:
                #     back -= 1

    return res

    #             res.add(tuple(sorted([nums[front], nums[back], nums[i]])))
    #             front += 1
    # return [list(el) for el in list(res)]
