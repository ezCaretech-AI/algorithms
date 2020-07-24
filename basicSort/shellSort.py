## 김영섭

def shellSort(a):
    h = 1
    n = len(a)-1
    while h < n:  ## 첫번째 간격 계산
        h = 3 * h + 1

    while h > 0:
        for i in range(h + 1, n + 1):
            v, j = a[i], i  ## v: value, j: index
            #             print(v,j,h,a[j-h])
            while j > h and a[j - h] > v:  ## 앞의 값 a[j-h]와 뒤의 값(v) 비교
                a[j] = a[j - h]  ## 값 교환
                j = j - h
            a[j] = v
        h = int(h / 3)  ## 간격 재 조정