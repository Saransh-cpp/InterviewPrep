
def longest_consecutive(arr):
    """brute -> better: can sort the array"""
    s = set(arr)
    largest_count = 1
    count = 1

    for el in s:
        if el - 1 in s:
            continue
        else:
            while el + 1 in s:
                count += 1
                el += 1
        if count > largest_count:
            largest_count = count
    return largest_count


if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2] 
    print(arr, longest_consecutive(arr))

    arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(arr, longest_consecutive(arr))

