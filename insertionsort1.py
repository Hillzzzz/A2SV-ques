def insertionSort1(n, arr):
    num_to_insert = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] > num_to_insert:
            arr[i + 1] = arr[i]
            print(*arr)
        else:
            arr[i + 1] = num_to_insert
            print(*arr)
            break
    if arr[0] > num_to_insert:
        arr[0] = num_to_insert
        print(*arr)
