
# Digital search tree란, 

## 1. 삽입 원칙
- 키의 최상위 비트부터 차례로 해당 비트가 0이면 왼쪽, 1이면 오른쪽으로 진행하여 외부 노드에 이르면 그 곳에 새로운 노드를 삽입

 ![Alt text](/imgs/Digital/digital_search_ex.jpg)

## 2. 탐색 원칙
- 원소의 비트에 따라 tree를 내려가며 하나씩 비교


## 3. 장단점
- 장점 : 구현이 간단함
- 단점 : tree를 내려가며 매번 키 값을 비교하기 때문에 탐색 키가 큰 경우에는 키 비교에 많은 시간이 소요되는 단점이 있음

## 4. 응용분야
- 네트워크 IP routing, packet classification, firewalls에서 사용됨

## 5. 시간 복잡도
> O(# bits in a key)

 Link: [다양한 알고리즘 ppt 링크][insertionSortlink]

[insertionSortlink]: http://inside.mines.edu/~dmehta/FDS_CPP/PPT/index.shtml "Go google"

