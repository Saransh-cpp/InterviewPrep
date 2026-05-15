def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break



if __name__ == "__main__":
    arr = [1, 3, 2, 6, 5, 8, 0, 9, 4]
    bubble(arr)
    print(arr)

    arr = [13, 46, 24, 52, 20, 9]
    bubble(arr)
    print(arr)

    arr = [5, 4, 3, 2, 1, 1]
    bubble(arr)
    print(arr)

    arr = [1, 2, 3, 4, 5]
    bubble(arr)
    print(arr)
