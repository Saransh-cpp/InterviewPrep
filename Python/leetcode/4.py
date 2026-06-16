def findMedianSortedArrays(nums1, nums2):
    n = len(nums1) + len(nums2)
    arr = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1

    if i < len(nums1):
        arr += nums1[i:]
    elif j < len(nums2):
        arr += nums2[j:]

    return arr[n // 2] if n & 1 else (arr[int(n / 2)] + arr[int((n / 2) - 1)]) / 2
