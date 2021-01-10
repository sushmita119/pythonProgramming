def mergeSort(arr):
    if len(arr) < 2:
        return

    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    # merge(left,right)
    n1 = len(left)
    n2 = len(right)
    i = j = k = 0
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


arr = [4, 8, 9, 2, 6, 0, 1]
mergeSort(arr)
print(*arr)
