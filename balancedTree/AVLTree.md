# 2-3-4 트리
<dl>
  <dt>1. 목적</dt>
  <dd>좌우 균형 맞지 않는 경우 탐색 시간 소모 발생</dd>
  <dd>이러한 트리 값 불균형 문제 해결을 위해 고안된 균형 트리 중 하나인 2-3-4 트리</dd>
  <br></br>
  <dt>2. 기본구조</dt>
  <dd>한 노드에 최대 3개 Key 가질 수 있음</dd>
  <dd>자식노드 최소 2개, 최대 4개 가질 수 있음</dd>
  <dd>모든 리프노드의 깊이는 동일</dd>
  <dd>부모와 동일 값 가진 데이터는 쌍방향 가능</dd>
  <br></br>
  <dt>3. 노드 명칭 의미</dt>
  <dd>2-노드 : Key 1개 + 2개 자식노드</dd>
  <dd>3-노드 : Key 2개 + 3개 자식노드</dd>
  <dd>4-노드 : Key 3개 + 4개 자식노드</dd>
  <br></br>

  ![Nodes](/imgs/Tree234/Nodes_1.png)
  <br></br>

  ![Nodes](/imgs/Tree234/Nodes_2.png)
  <br></br>
  <dt>4. OPERATION</dt>
  <dt>4.1 삽입(Insertion)</dt>
  <dd>추가하려는 Key 값 정해지면 루트노드부터 Key 값 탐색</dd>
  <dd>삽입은 항상 리프노드에서 수행</dd>
  <dd>Key를 3개 가지고 있는 4-노드의 경우 삽입이 불가하기 때문에 <b>삽입 이전 단계에서 4-노드 여부 판단하여 4-노드 분리 선행</b></dd>
   <br></br>
  
   ![Tree234 정렬 예시](/imgs/Tree234/Tree234_sort.png)
   <br></br>

   ![Tree234 정렬 예시](/imgs/Tree234/insert_1.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/insert_2.png)
   <br></br>

 <dt>4.2 분할(Split)</dt>
 <dd>3개 키를 갖는 4-노드의 경우</dd>
 <dd>부모노드 有 : 가운데 Key를 부모노드에 추가</dd>
 <dd>부모노드 無 : 가운데 Key를 뽑아 부모노드(2-노드)로 만들고(분할 선행) 나머지 2개의 2-노드를 별개의 자식노드로 만듦</dd>
 <dd>깊이 증가는 <b>루트노드</b>를 분할시에만 발생(cf. Binary search의 경우에는 리프 추가 시 깊이 증가)</dd>
 <dd>분할 시 리프 노드의 Key를 부모노드로 보내기에 앞서 부모노드 Key 값 탐색</dd>
 
   <br></br>
  <dt>4.3 삭제(Deletion)</dt>
  <dd>삭제할 값이 포함된 노드를 먼저 탐색</dd>
  <dd>삭제도 항상 리프노드에서 수행</dd>
  <dd>삭제하려는 Key가 리프노드에 있지 않은 경우 : Key의 predecessor/successor 포함하는 리프노드 검색한 후 자리바꿈</dd>
  <dd>삭제 대상이 2-노드에 포함된 경우 : 삭제시 유일한 Key가 삭제되기 때문에 리프노드가 3-노드/4-노드일 경우에만 가능. 삭제 대상 옆에 있는 3-노드/4-노드에서 Key 하나 가져옴(루트인 경우는 예외)</dd>
   <br></br>

   ![Tree234 정렬 예시](/imgs/Tree234/Tree234_delete.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/delete_1.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/delete_2.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/delete_3.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/delete_4.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/delete_5.png)
   <br></br>
   
   ![Tree234 정렬 예시](/imgs/Tree234/delete_6.png)
   <br></br>
  <dt>4.4 병합(Merge, fusion)</dt>
  <dd>한 부모 밑의 2-노드 형제인 경우, 부모노드에서 Key를 가져다가 새로운 4-노드 생성 가능(부모노드가 최소 두개 Key 보유 가정)</dd>
   <br></br>

   ![Tree234 정렬 예시](/imgs/Tree234/merge_1.png)
   <br></br>

<dt>5. 시간 복잡도</dt>
<dd>깊이 하나 당 소요 시간 : O(1)</dd>
<dd>트리 높이(연산과정 따라 문제 해결에 필요한 단계 감소) : O(log n)</dd>
<dd>시간 복잡도 : O(1) x O(log n) = O(log n)</dd>
<dd>최선 및 최악의 경우 : O(logn)</dd>
<dd>=> 메모리 및 시간 복잡도 성능 좋은 편</dd>
<br></br>

| Time Complexity       | Best case           | Worst case  |
| ------------- |:-------------:| -----:|
| B-Tree      | O(log n) | O(log n) |
| 2-3-4 Tree      | O(log n) | O(log n) |

<br></br>


<dt>REFERENCES</dt>
<dd>https://algorithmtutor.com/Data-Structures/Tree/2-3-4-Trees/</dd>
<dd>https://www.educative.io/page/5689413791121408/80001</dd>
<dd>https://tbc-python.fossee.in/convert-notebook/Sams_Teach_Yourself_Data_Structures_and_Algorithms_Analysis_in_24_Hours/chapter20_1.ipynb</dd>
<dd>https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet#emphasis</dd>
</dl>