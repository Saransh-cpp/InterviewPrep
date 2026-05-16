def longest_subarray(nums, k):
    left = 0
    summ = 0
    max_len = 0
    for right in range(len(nums)):
        summ += nums[right]
        if summ > k:
            summ -= nums[left]
            left += 1
        elif summ == k:
            if right - left + 1 > max_len:
                max_len = right - left + 1

    return max_len


if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, 9]
    k = 15
    print(nums, k, longest_subarray(nums, k))

    nums = [-3, 2, 1]
    k = 6
    print(nums, k, longest_subarray(nums, k))
