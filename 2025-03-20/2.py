stack = [] # 리스트방식의 텅 빈 스택 선언
top = -1 # 전역변수 top 선언
n = 10

def push(value):
  global top
  stack.append(value)
  top += 1 # top = top + 1
  print(f'push: {stack}')

def pop(value):
  global top
  for i in range(len(stack)):
    if stack[i] == value:
      stack.pop(i)
      top -= 1
      print(f'pop: {stack}')
      return
    elif len(stack) == 0:
      print("스택이 비어있습니다.")
      return
    elif stack[i] != value:
      print("해당 값이 스택에 없습니다.")
      return
    else: 
      print("잘못된 입력입니다.")
      return

if "__name__" == "__name__":
  while True:
    num = int(input("1: 삽입, 2: 삭제, 3: 종료 => "))
    if num == 1:
      value = int(input("삽입할 값: "))
      push(value)
    elif num == 2:
      value = int(input("삭제할 값: "))
      pop(value)
    elif num == 3:
      break
    else:
      print("잘못된 입력입니다.")
      continue

