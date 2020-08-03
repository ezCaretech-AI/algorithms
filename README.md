# algorithms



## * Link: [마크다운 사용법 참고 링크][markdownlink]

[markdownlink]: https://gist.github.com/ihoneymon/652be052a0727ad59601 "Go google"

## * 파이썬 naming 참고 사진
![Alt text](/imgs/python_naming.png)

## * 회의 중 naming 규칙

###   1. 모듈 파일 : 소문자로 시작
    예:) createLossFunction, create_loss_function

###   2. Class : 명사형; 정적이고 고유명사스럽게

###   3. Function : 동사 + 목적어

## 4. 시간/공간 복잡도
- 알고리즘의 성능을 알아보기 위해 두가지 방법이 있음
1. 성능 분석 (analysis) ← 추정 (복잡도는 여기에 속함)
2. 성능 측정 (measurement) ← 실제로 실행&측정
- 공간 복잡도
    - 실행 ~ 완료까지 필요한 총 저장 공간
    > Sa = Sc + Se
    - Sc : 고정 공간
        - 컴파일된 알고리즘 명령어
        - 단순 변수
        - 복잡 데이터 구조와 변수
        - 상수
    - Se : 가변 공간
        - 실행 과정에서 필요로 하는 공간
        - 순환 호출 할 때마다 추가로 필요한 공간 (런타임 스텍)

- 시간 복잡도
    - 실행 ~ 완료까지 필요한 총 시간
    > Ta = Tc + Te
    - Tc : 컴파일 시간 (고정적)
    - Te : 실행 시간 ← 점근적 표기법 사용 (O, Θ, Ω)
    > O(1) < O(logN) < O(N) < O(NlongN) < O(N^2) < O(N^3) < O(2^N) < O(N!)
    ![Alt text](/imgs/bigOgraph.png)

    - O(1) : 입력자료의 수에 관계 없이 일정한 실행 시간을 갖는 경우
    - O(logN) : 커다란 문제를 일정한 크기를 갖는 작은 문제로 쪼개느 경우
    - O(N) : 입력 자료 각각에 일정 정도의 동일한 처리르 할 경우
    - O(NlogN) : 커다란 문제를 일정한 크기로 쪼개어 각각 독립적으로 해결하고 나중에 다시 그것을 하나로 모으는 경우
    - O(N^2) : 이중루프내에 입력 자료를 처리하는 경우
    - O(N^3) : 삼중루프내에 입력 자료를 처리하는 경우
    - O(2^N) : 흔하지 않음

Link: [시간 복잡도 나타는 경우 링크][bigOlink1]

[bigOlink1]: https://skmagic.tistory.com/164 "Go google"

Link: [시간 복잡도 그래프 링크][bigOlink2]

[bigOlink2]: https://blog.tomclansys.com/50 "Go google"