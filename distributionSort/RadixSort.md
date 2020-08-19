# <span style='color:red'>분포에 의한 정렬</span>

## <span style='color:red;font-weight:bold'>2. 기수 정렬(Radix Sort)</span>

### 2.1. 기수 정렬 개념 요약

> 1. 리스트에 있는 원소들의 자릿수에 따라서 정렬하는 알고리즘

![Alt text](/imgs/Radix_sort1.PNG)

>> * 1의 자릿수를 기준으로 정렬
>> * 10의 자릿수를 기준으로 정렬
>> * 100의 자릿수를 기준으로 정렬
>> * . . . . 최대 자릿수를 기준으로 정렬

> 2. 시간복잡도는 O(N+K)로, K는 최대 자릿수의 길이

### 2.2. 구현

>> 일반적으로 각 자릿수를 오름차순으로 담기위해 Queue를 이용함.

>> 자릿수에 따른 Queue에 원소를 집어넣는다. (N번)

>> Queue에 있는 원소를 POP 하여 원소를 재배열 한다. (N번)
 
> <span style='color:red;font-weight:bold'> 1. 첫 번째 '1'의 자릿수를 기준으로 정렬 </span>

![Alt text](/imgs/Radix_sort2.PNG)

> <span style='color:red;font-weight:bold'> 2. 두 번째 '10'의 자릿수를 기준으로 정렬 </span>

![Alt text](/imgs/Radix_sort3.PNG)

> <span style='color:red;font-weight:bold'> 3. 세 번째 '100'의 자릿수를 기준으로 정렬 </span>

![Alt text](/imgs/Radix_sort4.PNG)

>> 최대 자릿수의 길이가 3이므로 총 3번 진행

### 2.3. 정리

>> 데이터끼리 직접적인 비교를 하여 정렬하는 알고리즘의 경우 시간복잡도는 O(logN)보다 작아질 수 없음.

>> 기수 정렬은 자릿수가 있는 데이터(정수,문자열 등)에서만 수행이 가능하며, 데이터끼리의 직접적인 비교 없이 정렬을 수행.

>> (십진수의 경우) 0~9까지의 자릿수를 담으므로 10개의 Queue(여기서는 Bucket)를 이용

>> 비교를 이용한 정렬이 아니기 때문에 k가 상수일 경우 시간복잡도가 O(N)으로, 퀵정렬보다 빠른 시간 복잡도가 나오는 것이 가능.

>> 다만 이 알고리즘은 자릿수가 적은 4바이트 정수등에서나 제대로 된 성능을 발휘할 수 있으며, 자릿수가 무제한에 가까운 문자열 정렬등에 사용할 경우 오히려 퀵정렬보다 느릴 수 있음 

>> 무엇보다도 Bucket(Queue)과 같은 추가 메모리가 필요하다는 단점 존재
