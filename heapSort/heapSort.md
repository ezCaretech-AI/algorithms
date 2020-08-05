힙 정렬 
====


## 1. 힙 정렬이란?
- 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법
- 과정 설명 \
    1. 정렬해야 할 n개의 요소들로 최대 힙을 만든다.
    2. 그 다음으로 한 번에 하나씩 요소를 힙에서 꺼내서 배열의 뒤부터 저장
    3. 삭제되는 요소들은 값이 감소되는 순서로 정렬되게 됨

## 2. 힙 정렬 그림
![Alt text](/imgs/heapsort1.png)
![Alt text](/imgs/heapsort2.png)


## 3. 힙 정렬 수도 코드
```python
heapSort(a[]){
    n ← a.length - 1
    for (i ← n/2; i ≥ 1; i ← i-1) do
        heapify(a, i, n)
    for (i ← n-1; i ≥ 1; i ← i-1) do
        a[1] ↔ a[i+1]
        heapify(a, 1, i)
}
heapify(a[], h, m){
    v ← a[h]
    for (j ← 2*h; j ≤ m; j ← j*2) do
        if (j < m and a[j] < a[j+1]) then j ← j+1
        if (v ≥ a[j]) then exit
        else a[j/2] ← a[j]
    a[j/2] ← v
}

```

## 3-1.  힙 정렬 코드

## 4. 힙 정렬 추가적인 특징들
### 4.1 공간 / 시간 복잡도
>공간 복잡도
> > 최선 : O(N) \
최악 : O(N)

>시간 복잡도
> >  최선 : O(𝑁logN) \
최악 : O(𝑁logN) \
평균 : O(𝑁logN)

### 4.2 장단점
> **장점** : 준수한 시간 내에 정렬한다. \
**단점** : 안정적이지 않다. \
안정성 있는 정렬 : 같은 값을 가진 데이터의 순서가 정렬 후에도 바뀌지 않고 그대로 유지하는 정렬

### 4.3 사용되는 경우
> 전체 자료를 정렬하는 것이 아니라 가장 큰 값 몇개만 필요할 때 유용하다.

### 4.4 힙 정렬 애니메이션
![힙 정렬](/imgs/heapsort_move1.gif)
![힙 정렬](/imgs/heapsort_move2.gif)