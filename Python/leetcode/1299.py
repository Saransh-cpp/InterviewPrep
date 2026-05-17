def replaceElements(arr):
    if len(arr) == 1: return [-1]
    res = [-1]
    curr_max = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i + 1] > curr_max:
            curr_max = arr[i + 1]
        res.append(curr_max)
    return res[::-1]


def replaceElements(arr):
    curr_max = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = curr_max
        if temp > curr_max: curr_max = temp
    return arr
