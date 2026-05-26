def all_subarray(nums, k):
    summ = 0
    count = 0
    d = {0: 1}
    for i in range(len(nums)):
        summ ^= nums[i]

        if k^summ in d:
            count += d[k^summ]
        d[summ] = 1 if summ not in d else d[summ] + 1

    return count


if __name__ == "__main__":
    nums = [4, 2, 2, 6, 4]
    k = 6
    print(nums, k, all_subarray(nums, k))

    nums = [5, 6, 7, 8, 9]
    k = 5
    print(nums, k, all_subarray(nums, k))
