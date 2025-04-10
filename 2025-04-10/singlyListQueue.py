class LinkedQueue:
  class Node:
    def __init__(self, item, next):  # node 클래스 멤버 함수
      self.item = item # parmaeter로 받은 item을 넣어줌
      self.next = next # parmaeter로 받은 next를 넣어줌
  
  # LinkedQueue의 생성자
  def __init__(self):
      self.front = None # 큐의 front를 None으로 초기화 
      self.rear = None # 큐의 rear를 None으로 초기화
      self.size = 0 # 큐의 크기를 0으로 초기화

  def isEmpty(self):
      return self.size == 0 # 큐가 비어있는지 확인하는 메서드
  
  # item을 큐에 추가하는 메서드
  def add(self, item):
    newnode = self.Node(item, None) # 새로운 노드 생성
    if self.isEmpty():
      self.front = newnode # 큐가 비어있을 때 front를 새 노드로 설정
    else:
      self.rear.next = newnode # 큐가 비어있지 않을 때 rear의 다음 노드를 새 노드로 설정
    
    self.rear = newnode # rear를 새 노드로 설정
    self.size += 1 # 큐의 크기 증가

  def showq(self):
    p = self.front
    print("front => ", end="")
    while p:
      if p.next != None:
        print("{!s:<7}".format(p.item), "->", end="")
      else:
        print(p.item, end="")
      p = p.next
    print(" <= rear")


if __name__ == "__main__":
  q = LinkedQueue() # 생성자 호출
  q.add("apple")
  q.add("orange")
  q.add("banana")
  q.showq()