# AVL 트리
<dl>
  <dt>1. 특징</dt>
  <dd>AVL 트리는 1962년 러시아의 수학자 Adelson-Velskii와 Landis가 
  'An algorithm for the organization of information' 논문을 통해 발표됐고, 그들의 이름을 따와서 지어졌다. AVL 트리는 이진탐색트리 처럼 트리가 한쪽으로 치우쳐 자라나는 현상을 방지하여 트리 높이의 균형을 유지하는 이진탐색트리이다. Balanced 이진탐색트리를 만들면 N개의 노드를 가진 트리의 높이가 O(log n)이 되어 탐색, 삽입, 삭제 연산의 수행시간이 O(log n)이 보장된다.</dd>
  <br></br>

  <dt>2. Binary Search Tree, Balanced Binary Tree 비교</dt>
  
  >* Binary Search Tree
  >>* 최선의 경우 아래 그림처럼 시간복잡도를 O(log n)로 줄일 수 있음
  >>* 하지만 Unbalanced Tree와 같이 최악 경우 탐색의 속도는 느려짐
  >>* 예를 들어 이진탐색트리에 정렬된 배열 [8,12,14,16,18]를 차례로 저장하면 아래와 같다.
  >>
  >>![Nodes](/imgs/binary_tree.png)
  >>
  >>* 이렇게 이진탐색트리에 정렬된 배열을 저장하면, 결국 연결리스트가 되고 시간 복잡도는 O(log n)이 아닌, O(n)이 된다.

  >* Balanced Binary Search Tree (Red-Black Tree, AVL Tree)
  >>* 이진트리가 균형을 이루도록 보장
  >>* 항상 O(log n)의 시간복잡도를 보장
  >>* Balance Binary Tree에 정렬된 배열 [8,12,14,16,18]를 차례로 저장하면 아래와 같다.
  >>
  >>![Nodes](/imgs/avl_tree.png)
  >>
  >>* 이렇게 Balance Binary Tree에 정렬된 배열을 저장하면,시간 복잡도는 O(log n)으로 보장된다.

  <br></br>
  <dt>3. AVL Tree의 특성</dt>
  
  > * 이진탐색트리 연산 실행시간은 이진탐색트리의 높이에 따라 달라지는데 최상의 성능을 얻으려면 트리의 균형을 유지해야한다.
  > * AVL 트리에서 노드의 두 하위 트리(왼쪽, 오른쪽)의 높이 차이는 아래 그림처럼 -1 ~ 1을 넘지 않아야 한다.
  > * AVL 트리는 엄격하게 균형을 유지하기 때문에 Red-black 트리보다 더 빠른 성능을 가지지만 더 많은 작업을 수행해야만 한다.
  > * 대부분의 연산은 이진탐색트리와 동일하다.
  > * 이진탐색트리와 동일하게 모든 노드는 최대 2개의 자식노드를 가질수 있고, 왼쪽 자식노드는 부모노드보다 작고, 오른쪽 자식노드는 크다.
  > * 삽입 연산의 경우 이진탐색트리와 동일하지만 모든 삽입연산은 트리가 균형을 유지하는지 확인을 해야한다.

  >> ![Nodes](/imgs/avl_tree_bf.png)
  <br></br>

  <dt>4. 동작</dt>
  <dt>AVL 트리에서 노드를 일반적인 이진 탐색 트리처럼 삽입, 삭제 시키면 높이 균형 성질을 만족하지 않게 된다. 노드가 삽입, 삭제가 될 때 회전을 통해 트리를 재구성하여 높이 균형 성질을 유지시킨다.</dt>
  <br></br>
  <dt>4.1 삽입(Insertion)</dt>
  <dd>AVL 트리 T에 새로운 노드 d를 삽입하는 경우, T에서 d가 리프 노드로 삽입될 수 있도록 하는 노드 w를 찾고 w의 자식으로 d를 삽입한다.</dd>
  <dd>d를 삽입하면 불균형해질수 있는데 세 노드를 기준으로 회전시킴으로써 균형을 맞춰준다.</dd>
   <br></br>
  
   ![Tree234 정렬 예시](/imgs/avl_tree_insert.png)
   <br></br>

<dt>5. 시간 복잡도</dt>
<dd>AVL 트리의 기본연산은 이진탐색트리와 동일하지만 아래의 표를 보면 시간 복잡도가 다르다.</dd>
<br>

| 이진탐색트리       | Best case           | Worst case  |
| ------------- |:-------------:| -----:|
| 공간      | O(log n) | O(n) |
| 삽입      | O(log n) | O(n) |
| 삭제      | O(log n) | O(n) |
| 탐색      | O(log n) | O(n) |

<br>

| AVL 트리       | Best case           | Worst case  |
| ------------- |:-------------:| -----:|
| 공간      | O(n) | O(n) |
| 삽입      | O(log n) | O(log n) |
| 삭제      | O(log n) | O(log n) |
| 탐색      | O(log n) | O(log n) |

<br></br>


<dt>REFERENCES</dt>
<dd>1. https://ko.wikipedia.org/wiki/AVL_%ED%8A%B8%EB%A6%AC</dd>
<br>
<dd>2. https://m.blog.naver.com/PostView.nhn?blogId=dhdh6190&logNo=221062784111&proxyReferer=http:%2F%2Fwww.google.com%2Furl%3Fsa%3Dt%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dweb%26cd%3D%26ved%3D2ahUKEwi5svTd4OrrAhWG7WEKHUeNCB8QFjAEegQIBBAB%26url%3Dhttp%253A%252F%252Fm.blog.naver.com%252Fdhdh6190%252F221062784111%26usg%3DAOvVaw2XbPUxafZ4GswOoCI3KpSr</dd>
<br>
<dd>3. https://www.zerocho.com/category/Algorithm/post/583cacb648a7340018ac73f1</dd>
<br>
<dd>4. https://ratsgo.github.io/data%20structure&algorithm/2017/10/27/avltree/</dd>
</dl>