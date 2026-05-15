def insertion(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            j = i - 1
            while (arr[j + 1] < arr[j] and j >= 0):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1



if __name__ == "__main__":
    arr = [1, 3, 2, 6, 5, 8, 0, 9, 4]
    insertion(arr)
    print(arr)

    arr = [13, 46, 24, 52, 20, 9]
    insertion(arr)
    print(arr)

    arr = [5, 4, 3, 2, 1, 1]
    insertion(arr)
    print(arr)

    arr = [1, 2, 3, 4, 5]
    insertion(arr)
    print(arr)
