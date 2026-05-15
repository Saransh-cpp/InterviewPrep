def unionOfSorted(nums1, nums2):
    i = 0
    j = 0
    union = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1
        elif nums1[i] == nums2[j]:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1
            j += 1

    while i < len(nums1):
        if union[-1] != nums1[i]:
            union.append(nums1[i])
        i += 1

    while j < len(nums2):
        if union[-1] != nums2[j]:
            union.append(nums2[j])
        j += 1

    return union


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [2, 3, 4, 4, 5]
    print(nums2, nums1, unionOfSorted(nums1, nums2))

    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums2 = [2, 3, 4, 4, 5, 11, 12]
    print(nums2, nums1, unionOfSorted(nums1, nums2))
