# 일반적인 퀵정렬
def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr
        
arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
print(quick_sorted(arr))



# 매번 리스트를 생성하지 않고 inplace sorting 방식으로 
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

# left : 정렬 대상의 가장 왼쪽 지점을 가리키는 이름
# right : 정렬 대상의 가장 오른쪽 지점을 가리키는 이름
# mid(pivot) : 피벗이라 발음하고 중심점, 중심축의 의미
# low : 피벗을 제외한 가장 왼쪽에 위치한 지점을 가리키는 이름
# high : 피벗을 제외한 가장 오른쪽에 위치한 지점을 가리키는 이름


# https://wogh8732.tistory.com/9