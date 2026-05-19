def longest_subarray(nums):
    summ = 0
    max_len = 0
    d = {}
    for i in range(len(nums)):
        summ += nums[i]
        if summ == 0:
            if i + 1 > max_len:
                max_len = i + 1
        elif summ not in d:
            d[summ] = i
        else:
            if i - d[summ] > max_len:
                max_len = i - d[summ]

    return max_len


if __name__ == "__main__":
    nums = [9, -3, 3, -1, 6, -5]
    print(nums, longest_subarray(nums))

    nums = [6, -2, 2, -8, 1, 7, 4, -10]
    print(nums, longest_subarray(nums))
