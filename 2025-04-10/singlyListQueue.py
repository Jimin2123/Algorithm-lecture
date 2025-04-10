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
    if self.isEmpty():
      print("큐가 비어있음")
      return None

    p = self.front
    print("front => ", end="") # 큐의 front를 출력
    
    while p:
      if p.next != None: # 다음 노드가 있을 때
        print("{!s:<7}".format(p.item), "->", end="")
      else:
        print(p.item, end="")
      p = p.next
    print(" <= rear")

  def remove(self):
    if self.isEmpty():
      raise EmptyError("queue안에 아무것도 없음")
    else:
      fitem = self.front.item # front의 item을 fitem에 저장
      prefront = self.front # 삭제할 item을 prefront에 저장
      self.front = self.front.next # front를 다음 노드로 이동
      self.size -= 1 # 인덱스 사이즈 감소
      del prefront # 삭제
      if self.isEmpty():
        self.rear = None # 큐가 비어있을 때 rear를 None으로 설정
      return fitem # 삭제한 item을 반환

class EmptyError(Exception):
  pass

if __name__ == "__main__":
  q = LinkedQueue() # 생성자 호출
  q.add("apple")
  q.add("orange")
  q.add("banana")
  q.showq()

  removeItem = q.remove()
  print("front인 사과 삭제 후 removeItem: ", removeItem)
  q.showq()

  removeItem = q.remove()
  print("front인 사과 삭제 후 removeItem: ", removeItem)
  q.showq()

  removeItem = q.remove()
  print("front인 사과 삭제 후 removeItem: ", removeItem)
  q.showq()
