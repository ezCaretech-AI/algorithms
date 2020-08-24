## 김영섭

def insertionSort_ASC(arr, first, last, h):
    i = first + h
    
    while i<= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos-h] > val:
            arr[pos] = arr[pos-h]
            pos = pos - h
        arr[pos] = val
        i = i + h

def shellSort(arr):
    n = len(arr)
    h = n//2
    while h > 0:
        for i in range(0, h):
            insertionSort_ASC(arr, i, n-1, h)
        h //= 2
        
    return arr