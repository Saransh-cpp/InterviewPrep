def selection(arr):
    for i in range(len(arr) - 1):
        mini = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]


if __name__ == "__main__":
    arr = [1, 3, 2, 6, 5, 8, 0, 9, 4]
    selection(arr)
    print(arr)

    arr = [13, 46, 24, 52, 20, 9]
    selection(arr)
    print(arr)

    arr = [5, 4, 3, 2, 1, 1]
    selection(arr)
    print(arr)
