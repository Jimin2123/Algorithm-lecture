from collections import deque

# 카드 개수 입력
N = int(input("카드의 개수 N을 입력하세요: "))

# 1부터 N까지 카드를 큐에 저장
myQueue = deque(range(1, N + 1))
step = 1; # 단계 초기화

# 카드가 1장 남을 때까지 반복
while len(myQueue) > 1:
    # 맨 위의 카드를 버림
    removed = myQueue.popleft()
    # 그 다음 맨 위의 카드를 아래로 이동
    moved = myQueue.popleft()
    myQueue.append(moved)
    print(f"Step {step}: 버림={removed}, 이동={moved}, 현재 상태={list(myQueue)}")
    step += 1

# 마지막으로 남은 카드 출력
print("마지막으로 남은 카드:", myQueue[0])

