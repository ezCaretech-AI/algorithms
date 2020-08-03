# <span style='color:red'>쉘 정렬(shellsort)</span>

### <span style='color:blue'>1. 이론적 배경</span>
> 1. 쉘 정렬은 삽입 정렬의 단점을 보완한 방법.
> 2. 삽입정렬을 이용하여 리스트 전체에 대해 작업하는 대신 서브리스트로 나누어 각 서브리스트에 삽입 정렬을 적용.
> 3. 서브리스트를 나누는 방법은 일정한 간격 순차를 사용. (홀수와 짝수가 번갈아 가면서 진행해야 함)
> 4. 이런 과정을 반복하다가 간격이 1이되면 마지막에는 리스트 전체에 대해 삽입 정렬을 수행.

### <span style='color:blue'>2. 주요 특징</span>
> * 삽입정렬의 단점인 원소의 비교 연산과 먼 거리의 원소 이동을 줄일 수 있다.
>> * 삽입정렬의 단점 : 요소들이 삽입될 때, 이웃한 위치로만 이동, 즉 삽입할 위치가 현재 위치에서 상당히 멀리 떨어진 곳이라면 많은 이동을 해야함.
>> * 삽입정렬과 다르게 쉘 정렬은 전체의 리스트를 한번에 정렬하지 않음.

### <span style='color:blue'>3. 정렬 순서</span>

![shellSort1.png](/imgs/shellSort1.PNG)

### <span style='color:blue'>4. Index 계산 방법</span>
> 1. 간격(Gap)을 계산하는 방법은 여러가지가 있음
>> * (정렬한 값의 개수) / 2
>> * (1093, 364, 121, 40, 13, 4, 1)와 같은 인덱스

### <span style='color:blue'>5. 실행 결과</span>

<pre>
<code>

import random
import time

def shellSort(a, n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h+1, n+1):
            v, j = a[i], i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j = j -h
            a[j] = v
        h = int(h/3)

N = 5000

a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time
print('쉘 정렬의 실행 시간(N=%d) : %0.3f'%(N, end_time))



</code>
</pre>

>> <span style='color:red'>쉘 정렬의 실행 시간(N=5000) : 0.018 ->  선택 정렬, 버블 정렬, 삽입 정렬에 비해 매우 빠름.</span>