## 퀵정렬(Quick Sort)

#### 특징 
- 타원소와의 비교만으로 정렬하는 비교 정렬
- 분할 정복(divide and conquer) 알고리즘
- 문제를 2개로 분리 후 각각 해결 => 결과 모아서 원래 문제 해결
- 재귀 호출 진행될 때마다 최소 하나(피벗)은 최종적으로 위치가 정해지는 특징
- 리스트 비균등 분할 (cf. merge sort : 리스트 균등 분할)
- 데이터 쪼개면서 정렬 (cf. merge sort : 데이터 쪼갠 뒤 합치면서 정렬)
- 내장 정렬함수(i.e., list.sort(), Arrays.sort()) 등이 퀵정렬 기반으로 구현됨

#### 분할 정복 알고리즘 
- 분할(Divide) : 입력 배열을 피벗 기준 비균등하게 2개 부분 배열로 분할
- 정복(Conquer) : 부분 배열을 정렬. 부분 배열 크기가 충분히 작지 않으면 순환 호출하여 분할 정복 재적용
- 결합(Combine) : 정렬된 부분 배열들을 하나의 배열에 병합

#### 단계별 과정
- 리스트 내 하나의 요소(피벗) 선택
- 피벗보다 작은 요소들 피벗 왼쪽으로
- 피벗보다 큰 요소들 피벗 오른쪽으로
- 피벗 제외하고 왼쪽 리스트와 오른쪽 리스트를 재정렬
- 분할된 부분 리스트에 대하여 순환 호출로 정렬 반복 수행
- 부분 리스트에서도 피벗 정하고 피벗 기준 왼쪽 리스트/오른쪽 리스트로 나누는 과정 반복
- 부분 리스트의 분할 가능할 때까지 반복(리스트 크기가 0 또는 1 될때까지)

#### 장점
- 불필요한 데이터 이동 줄이고 원거리 데이터 교환하기 때문에 수행 속도 빠름
- 한번 결정된 피벗들이 추후 연산에서 제외되어 수행 속도 빠름
- 최선 성능 낼때는 병합정렬, 힙정렬보다 빠름 

#### 단점
- 매 재귀 호출 시 새로운 리스트를 생성하여 리턴 => 메모리 측면 비효율 
- 비정렬 상태에서 동일 키값 원소 순서가 정렬 후에도 유지되지 않는 불안정 정렬
- 피벗 값이 같은 것끼리 순서관계가 파괴

#### 코드 및 개념 도식화

![Screenshot](/imgs/imgs_quicksort/quicksort_2.png)

- 일반적인 경우
![Screenshot](/imgs/imgs_quicksort/quicksort_python_1.png)


- inplace sorting 방식의 파이썬 코드

![Screenshot](/imgs/imgs_quicksort/quicksort_python_2.png)

- 리스트의 정 가운데 있는 값을 pivot 값을 선택
- left : 정렬 대상의 가장 왼쪽 지점을 가리키는 이름
- right : 정렬 대상의 가장 오른쪽 지점을 가리키는 이름
- mid(pivot) : 피벗이라 발음하고 중심점, 중심축의 의미
- low : 피벗을 제외한 가장 왼쪽에 위치한 지점을 가리키는 이름
- high : 피벗을 제외한 가장 오른쪽에 위치한 지점을 가리키는 이름

#### 시간 복잡도

![Screenshot](/imgs/imgs_quicksort/time_complexity.png)

#### 최선의 경우
- O(nlog2n) = 순환 호출 깊이(log2n) x 마지막 부분 배열 개수(n)
- 각 순환 호출에서 전체 리스트 대부분 레코드를 비교해야 하므로 평균 n번 비교 수행 

![Screenshot](/imgs/imgs_quicksort/quicksort_best.png)

#### 평균의 경우
- O(nlog2n)
- 시간 복잡도가 O(nlog2n)인 타 정렬 알고리즘 중에서 가장 빠름

#### 최악의 경우
- O(n^2)
- 분할 시 값들이 한 편으로 크게(모두) 치우친 경우
- 특히 이미 정렬된 리스트에 대하여 퀵 정렬을 실행할 경우

![Screenshot](/imgs/imgs_quicksort/quicksort_worst.png)

#### 공간 복잡도
- 데이터 복제가 필요없는 inplace 알고리즘
- 그러나 데이터 복제하여 O(n)의 추가 메모리 사용하는 방식으로 구현한 코드 다수(구현 방법에 따라 달라지는 사례)
- 입력 배열이 차지하는 메모리만 사용하는 inplace sorting 방식으로 구현할 경우 O(1)

#### References
- https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html
- https://wogh8732.tistory.com/9
