from heapSort import heapify

def heapSort(input_array):
    n = len(input_array)
    # BUILD-MAX-HEAP (A) : 위의 1단계
    # 인덱스 : (n을 2로 나눈 몫-1)~0
    # 최초 힙 구성시 배열의 중간부터 시작하면 
    # 이진트리 성질에 의해 모든 요소값을 
    # 서로 한번씩 비교할 수 있게 됨 : O(n)
    for i in range(n//2-1, -1, -1):
        heapify.heapify(input_array, i, n)
    # Recurrent (B) : 2~4단계
    # 한번 힙이 구성되면 개별 노드는
    # 최악의 경우에도 트리의 높이(logn)
    # 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 : O(nlogn)
    for i in range(n - 1, 0, -1):
        input_array[0], input_array[i] = input_array[i], input_array[0]
        heapify.heapify(input_array, 0, i)
    return input_array