def longestOnes(nums, k):
    max_len = 0
    length = 0
    r = 0
    l = 0
    cnt = 0
    while r < len(nums):
        if nums[r] == 1:
            length += 1
            max_len = max(max_len, length)
            r += 1
        else:
            if k == cnt:
                while nums[l] != 0:
                    l += 1
                l += 1
                length = r - l + 1
            else:
                length += 1
                max_len = max(max_len, length)
                cnt += 1
            r += 1
    return max_len


def longestOnes(nums, k):
    length = 0
    r = 0
    l = 0
    cnt = 0
    while r < len(nums):
        if nums[r] == 0: cnt += 1
        if cnt > k:
            if nums[l] == 0:
                cnt -= 1
            l += 1
        if cnt <= k:
            length = max(length, r - l + 1)
        r += 1

    return length
