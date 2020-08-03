합병 정렬 
====


## 1. 합병 정렬이란?
배열을 두개로 쪼개어 각각 정렬하고 합치는 정렬이다. \
예를 들어 리스트 A = [6, 2, 8, 1, 3, 9] 가 있을 때, \
L = [6, 2, 8] 과 R = [1, 3, 9] 로 나눈다. 그리고 각각의 리스트를 정렬한다. \
L = [2, 6, 8] 과 R = [1, 3, 9] 정렬된 두 리스트를 합친다. \
S = [1]  <span style='color:green'>← min(L[0], R[0])</span> \
S = [1, 2] <span style='color:green'> ← min(L[1], R[0])</span> \
S = [1, 2, 3] <span style='color:green'> ← min(L[1], R[1])</span> \
S = [1, 2, 3, 6] <span style='color:green'> ← min(L[1], R[2])</span> \
S = [1, 2, 3, 6, 8] <span style='color:green'> ← min(L[2], R[2])</span> \
S = [1, 2, 3, 6, 8, 9] <span style='color:green'> ← R[2]</span>




## 2. 합병 정렬 그림
![Alt text](/imgs/mergesort.png)


## 3. 합병 정렬 수도 코드
```c++
mergeSort(a[]){
    mid = len(a)/2
    leftArray = a[:mid]
    rightArray = a[mid:]
    mergeSort(leftArray)
    mergeSort(rightArray)
    a = merge(leftArray, rightArray)
}

merge(left[], right[]){
    정렬된 두 배열 left[]와 right[]를 합병
    정렬된 하나의 배열을 리턴한다.
}
```
## 4. 합병 정렬 추가적인 특징들
### 4.1 공간 / 시간 복잡도
>공간 복잡도
> > 최선 : O(N) \
최악 : O(N)

>시간 복잡도
> >  최선 : O(𝑁logN) \
최악 : O(𝑁logN) \
평균 : O(𝑁logN)

### 4.2 장단점
> **장점** : 안정적으로 준수한 시간 내에 정렬한다. \
**단점** : 추가적인 메모리가 필요하다. 배열의 크기가 클 경우 부담이 될 수 있다.

### 4.3 합병 정렬 애니메이션
![합병 정렬](/imgs/mergesort_move.gif)