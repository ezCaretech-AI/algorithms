## 선택정렬(Selection Sort)
#### 특징 
- 정렬되지 않은 전체 자료 중에서 해당 위치에 맞는 자료를 선택하여 위치 교환하는 정렬 방식
- 비교 연산 및 이동 연산 횟수가 고정된 값 => 연산 횟수 측면에서 정렬기법 중 최악
- 내림 차순으로 정렬되어 있는 자료를 오름 차순으로 재정렬할 때 최적. 반대 경우 최악  
- 추가 공간 불필요, inplace로 정렬

#### 단계별 과정
- 정렬되지 않은 수를 차례대로 비교하면서 가장 작은 수를 찾음 
- 가장 작은 수와 정렬되지 않은 수 목록 중 가장 첫번째 수를 교환. 교환한 수(가장 작은 수)는 정렬된 수로 간주
- 정렬되지 않은 목록을 가지고 모든 수가 정렬될 때까지 위 과정을 반복

#### 주요 아이디어 
- 주어진 수들은 애초에 정렬되지 않은 수 (같은 값의 인덱스끼리도 교환 연산 발생)
- 정렬 과정에서 정렬된 수와 정렬되지 않은 수로 나뉨

#### 장점
- 구현이 쉬움  
- 정렬 진행됨에 따라 속도 빨라짐
- 비교 연산 횟수는 많지만 실제 교환하는 횟수는 적음 => 많은 교환이 일어나야 하는 자료상태에서 가장 효율적 
- i 루프 한번에 교환 횟수가 1번을 넘기지 않음 => 버블정렬은 비교할 때마다 교환하기 때문에 자료의 크기가 클 경우 버블 정렬보다 효율적일 수 있음  

#### 단점
- 느려서 효율성 떨어짐
- 데이터 크기가 커질수록 효율 떨어짐
- 데이터 정렬 속도가 고정적으로 N 제곱만큼 걸리기 때문에 더 이상의 정렬 속도 기대하기 어려움 
- 이미 정렬된 상태에서 소수 자료 추가되면 재정렬 시 처리 속도 최악 

#### 코드 및 개념 도식화
- 검색 시작시점은 배열 인덱스 0부터, 진행순서에 따라 시작시점 인덱스 1씩 증가 

![Screenshot](/imgs/selection-sort.png)


![Screenshot](/imgs/selectionsort_python.png)

#### Time Complexity
- O(N^2)
- (N-1)+(N-2)+ ... +1 = (N*(N-1))/2 = (N^2 – N)/2
- N swaps result in the overall complexity of O(N^2) as there are two nested loops.

#### Best-case performance 
- О(N^2) comparisons, O(1) swaps

#### Worst-case performance 
- О(N^2) comparisons, О(n) swaps

#### Average performance 
- О(N^2) comparisons, О(n) swaps

#### Space complexity
- O(1), O(N)?

#### Worst-case space complexity 
- O(1)
