from mergeSort import merge

def mergeSort(input_array):
    if len(input_array) <= 1:
        return input_array
    mid = len(input_array) // 2
    leftArray = input_array[:mid]
    rightArray = input_array[mid:]
    input_array[:mid] = mergeSort(leftArray)
    input_array[mid:] = mergeSort(rightArray)
    input_array[:] = merge.merge(input_array[:mid], input_array[mid:])
    # print(input_array)
    return input_array
