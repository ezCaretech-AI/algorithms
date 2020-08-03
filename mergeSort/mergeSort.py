from mergeSort import merge

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftArray = arr[:mid]
    rightArray = arr[mid:]
    arr[:mid] = mergeSort(leftArray)
    arr[mid:] = mergeSort(rightArray)
    arr[:] = merge.merge(arr[:mid], arr[mid:])
    # print(arr)
    return arr
