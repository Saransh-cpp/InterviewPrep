def merge(nums1, m, nums2, n):
    nums1[:] = nums1[:m] + nums2[:n]
    nums1[:] = sorted(nums1)


def merge(nums1, m: int, nums2, n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0: return
    if m == 0: nums1[0] = nums2[0]
    end_idx = len(nums1) - 1
    m -= 1
    n -= 1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[end_idx] = nums1[m]
            m -= 1
            end_idx -= 1
        else:
            nums1[end_idx] = nums2[n]
            n -= 1
            end_idx -= 1
    for i in range(n + 1):
        nums1[i] = nums2[i]

