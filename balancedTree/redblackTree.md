# Red-Black Tree란,
- 이진 탐색 트리의 단점을 보완하기 위해 만들어진 균형 트리 중 하나
- 균형 트리 중 2-3-4 트리의 단점을 극복하기 위해 제안됨
- 


# 1. Red-Black Tree 생성시 원칙

 1. Root Property : 루트노드의 색깔은 검정(Black)이다.

 2. External Property : 모든 external node들은 검정(Black)이다.

 3. Internal Property : 빨강(Red)노드의 자식은 검정(Black)이다. 

 -  No Double Red(빨간색 노드가 연속으로 나올 수 없다.) 

 4. Depth Property : 모든 리프노드에서 Black Depth는 같다. 

 - 리프노드에서 루트노드까지 가는 경로에서 만나는 블랙노드의 개수는 같다. 



# 2. Double Red를 해결하는 전략이 2가지 

### 현재 insert된 노드의 uncle node의 색깔에 따라 수행하는 프로시저가 다릅니다. 

## 2-1. w가 검정(Black) 일 땐 Restructuring.
### ● Restructuring
 1. 나(z)와 내 부모(v), 내 부모의 부모(Grand Parent)를 오름차순으로 정렬

 2. 무조건 가운데 있는 값을 부모로 만들고 나머지 둘을 자식으로 만든다.

 3. 올라간 가운데 있는 값을 검정(Black)으로 만들고 그 두자식들을 빨강(Red)로 만든다. 

## 2-2. w가 빨강(Red)일 땐 Recoloring
### ● Recoloring
 1. 현재 inset된 노드(z)의 부모와 그 형제(w)를 검정(Black)으로 하고 Grand Parent(내 부모의 부모)를 빨강(Red)로 한다.

 2. Grand Parent(내 부모의 부모)가 Root node가 아니었을 시 Double Red가 다시 발생 할 수 있다.