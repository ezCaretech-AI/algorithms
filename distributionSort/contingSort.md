# <span style='color:red'>분포에 의한 정렬</span>

## <span style='color:red;font-weight:bold'>1. 계수 정렬(Counting Sort)</span>

### 2.1. 계수 정렬 개념 요약

> 1. 원소간 비교없이 정렬할 수 있는 정렬 알고리즘

>> * 원소간 비교하지 않고 각 원소가 몇개 등장하는지 갯수를 세서 정렬하는 방법
>> * 모든 원소는 양의 정수여야 함
>> * 시간복잡도는 O(n+k) (k는 정렬할 수들 중에 가장 큰 값을 의미함)로 퀵정렬, 병합정렬에 비해 일반적으로 빠르다.
>> * 정렬을 위한 길이 n의 배열하나, 계수를 위한 길이 k의 배열 하나. O(n+k)의 공간 복잡도를 가진다.

### 2.2. 구현

![Alt text](/imgs/countingSort1.jpg)

![Alt text](/imgs/countingSort2.jpg)

![Alt text](/imgs/countingSort5.jpg)

![Alt text](/imgs/countingSort3.jpg)

![Alt text](/imgs/countingSort4.jpg)



### 2.3. 정리

>> 계수 정렬은 이전에 알아본 알고리즘 비교 정렬이 아님

>> 이전까지는 두 수를 비교하여 정렬했다면 이 방법은 단 하나의 비교도 일어나지 않는다.

>> 정렬할 때 추가적인 메모리 (숫자 개수를 저장할 공간, 결과를 저장할 공간)가 필요하다는 점과, 가장 큰 숫자에 영향을 받는다는 점이 단점