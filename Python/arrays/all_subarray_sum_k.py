def all_subarray(nums, k):
    summ = 0
    count = 0
    d = {0: 1}
    for i in range(len(nums)):
        summ += nums[i]

        if summ - k in d:
            count += d[summ - k]
        d[summ] = 1 if summ not in d else d[summ] + 1

    return count


if __name__ == "__main__":
    nums = [3, 1, 2, 4]
    k = 6
    print(nums, k, all_subarray(nums, k))

    nums = [1, 2, 3]
    k = 3
    print(nums, k, all_subarray(nums, k))
