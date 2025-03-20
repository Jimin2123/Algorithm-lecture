# Stack & Queue

## Stack

- stack은 삽입과 삭제 연산이 후입선출(LIFO: Last-In First-out)로 이뤄지는 자료구조이다.
- 스택은 깊이 우선 타색(DFS: Depth First Serach), 백트래킹 종류의 코딩 테스트에서 효과적이다.

### 연산 (리스트 이름 : s)

- s.append(data) : top위치에 새로운 데이터 삽입
- s.pop() : top위치에 현재 데이터를 삭제,확인
- s[-1] : top위치에 현재 있는 데이터를 단순 확인

---

## Queue

- 큐는 삽입과 삭제 연산이 선입선출(FIFO)로 이뤄지는 자료구조
- 큐는 너비 우선 탐색(BFS: Breadth First Search)에서 자주 사용된다

### 연산 (리스트 이름 : s)

- s.apeend(data) : rear(마지막) 부분에 새로운 데이터를 삽입
- s.popleft() : front(처음) 부분에 있는 데이터를 삭제,확인
- s[0] : 큐의 front에 있는 데이터를 확인
