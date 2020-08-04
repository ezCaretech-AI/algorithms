# <span style='color:red'>버블 정렬(Bubble sort)</span>

### <span style='color:red'>1. 버블 정렬 알고리즘의 개념 요약</span>
> 1. 인접한 두 원소의 값을 비교해서 일정한 기준을 만족하면 서로의 값을 교환하여 정렬하는 알고리즘
>> * 예를 들어, 오름차순으로 정렬을 한다고 했을때, 두 항목의 값을 비교하여 앞쪽 값이 더 크면 두 항목의 값을 교환한다.

### <span style='color:red'>2. 버블 정렬 알고리즘의 예제</span>
> * 배열에 7, 4, 5, 1, 3이 저장되어 있다고 가정하고 자료를 오름차순으로 정렬해 보자.
>
> ![bubbleSort1.png](/imgs/bubbleSort1.PNG)
> 1. 1회전
>> * 첫 번째 원소 7을 두 번째 원소 4와 비교하여 교환하고, 두 번째의 7과 세 번째의 5를 비교하여 교환하고, 세 번째의 7과 네 번째의 1을 비교하여 고환하고, 네 번째의 7과 다섯 번째의 3을 비교하여 교환한다. 이 과정에서는 원소가 5개 이므로 원소를 4번 비교한다. 1회전 결과 가장 큰 원소가 맨 끝으로 Fix 되므로, 다음 회전에서는 맨 끝에 있는 자료는 비교할 필요가 없다.
> 2. 2회전
>> * 첫 번째 4를 두 번째 5와 비교하여 교환하지 않고, 두 번째 5와 세 번째의 1을 비교하여 교환하고, 세 번째의 5와 네 번째의 3을 비교하여 교환한다. 이 과정에서는 남아 있는 원소가 4개 이므로 원소를 세 번 비교한다. 비교한 자료 중 가장 큰 자료가 끝에서 두 번째에 놓인다.
> 3. 3회전
>> * 첫 번째의 4를 두 번째 1과 비교하여 교환하고, 두 번째의 4와 세 번째의 3을 비교하여 교환한다. 이 과정에서 자료를 두 번 비교한다. 비교한 자료 중 가장 큰 자료가 끝에서 세 번째에 놓인다.
> 4. 4회전
>> * 첫 번째의 1과 두 번째의 3을 비교하여 교환하지 않는다.

### <span style='color:red'>3. 버블 정렬 파이썬 코드</span>
<pre>
<code>
import random
import time

def bubbleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

N = 5000

a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time
print('버블 정렬의 실행 시간(N=%d) : %0.3f'%(N, end_time))
</code>
</pre>

>> <span style='color:red'>버블 정렬의 실행 시간 (N=5000) : 2.590 다른 정렬 알고리즘 보다 실행 시간이 오래 걸림.</span>

### <span style='color:red'>4. 버블 정렬 알고리즘의 특징</span>
> * 장점
>> * 구현이 매우 간단하다.
> * 단점
>> * 비교, 교환 작업이 너무 많아서 연산 시간이 오래 걸린다.

### <span style='color:red'>5. 버블 정렬의 시간복잡도</span>
> * 비교 횟수
>> * 최상, 평균, 최악 모두 일정
>> * EX) 원소가 N개인 배열일때, N-1, N-2, .... , 2, 1 번 = N(N-1)/2 번 비교
>> * N이 5일 때 비교 횟수를 계산해보면 5*(5-1)/2 = 10 -> 10번 비교
> * 교환 횟수
>> * 입력 자료가 역순으로 정렬되어 있는 최악의 경우, 한 번 교환하기 위하여 3번의 이동(SWAP 함수의 작업)이 필요하므로 (비교 횟수 * 3)번 = N(N-1)/2
>> * 입력 자료가 이미 정렬되어 있는 최상의 경우, 자료의 이동이 발생하지 않는다.
> * T(N) = O(N^2)의 시간 복잡도를 가지게 된다.

### <span style='color:red'>6. 정렬 알고리즘 시간복잡도 비교</span>
> ![bubbleSort2.png](/imgs/bubbleSort2.PNG)
> * 단순(구현 간단)하지만 비효율적인 방법
>> * 삽입 정렬, 선택 정렬, 버블 정렬
> * 복잡하지만 효율적인 방법
>> * 퀵 정렬, 힙 정렬, 합병 정렬, 기수 정렬

### <span style='color:red'>7. 결론</span>
> * 처음 정렬 개념을 배울 때 가르치는 용도로 적합, 하지만 성능 면에서는 효과적이지 않기 때문에 버블 정렬은 실제 업무에서는 사용되지 않는다. 즉, 버블 정렬은 교육적인 목적이 큰 정렬 방식이다.