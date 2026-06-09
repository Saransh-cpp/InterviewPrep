def findKthPositive(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) >> 1
        if arr[mid] - (mid + 1) < k:
            low = mid + 1
        else:
            high = mid - 1

    return k + high + 1
