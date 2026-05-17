def leaders(arr):
    res = [arr[-1]]
    curr_max = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        if res[-1] != curr_max:
            res.append(curr_max)
        if arr[i] > curr_max:
            curr_max = arr[i]
    return res[::-1]


if __name__ == "__main__":
    arr = [4, 7, 1, 0]
    print(arr, leaders(arr))

    arr = [10, 22, 12, 3, 0, 6]
    print(arr, leaders(arr))
