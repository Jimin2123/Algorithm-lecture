# 문제 [011] 스택으로 수열 만들기
# 1부터 n까지의 수를 스택에 저장하고 출력하는 방식으로 하나의 수열을 만들 수 있다.
# 이때 스택에 push하는 순서는 반드시 오름차순이어야 한다.
# 수열이 주어졌을 때 이러한 방식으로 스택을 이용해 주어진 수열을 만들 수 있는지 확인
# 만들 수 있다면 어떤 순서로 push와 pop을 수행해야 하는지 출력하고 확인하는 프로그램 작성

# 입력
# 1번째 줄에 수열의 개수 n이 주어진다. (1 <= n <= 100,000)
# 2번째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 주어진다.
# 이때 같은 정수가 두번 이상 나오지 않는다.

# 출력
# 수열을 만들기 위한 연산 순서를 출력한다.
# push 연산은 +로, pop연산은 -로 표현한다.
# 불가능한 경우 NO를 출력한다.

def make_sequence(n, sequence):
    stack = []
    result = []
    current = 1
    for num in sequence:
        # 현재 스택의 마지막 값이 원하는 값보다 작은 경우 push
        while current <= num:
            stack.append(current)
            result.append("+")
            current += 1
        
        # 스택의 top이 원하는 값과 같은 경우 pop
        if stack and stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            # 원하는 값이 스택에서 나올 수 없는 경우
            return ["NO"]
    
    return result

if __name__ == "__main__":
    n = int(input("수열의 개수를 입력하세요: "))
    
    print("수열을 이루는 숫자를 한 줄씩 입력하세요:")
    sequence = [int(input()) for _ in range(n)]
    
    result = make_sequence(n, sequence)
    
    for op in result:
        print(op)