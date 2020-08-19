import random, time

def countingSort(a):
    
    count = [0 for _ in range(max(a)+1)]   # 최댓값
    result = [0 for _ in range(len(a))]  # data 길이만큼
    
    for i in a:
        count[i] += 1   # data 요소의 출현 횟수

    for i in range(len(count)-1):
        count[i+1] += count[i]  # 누적 count

    for i in range(len(a)-1, -1, -1):
        result[count[a[i]] - 1] = a[i]
        count[a[i]] -= 1
    
    for i in range(len(result)):
        a[i] = result[i]

