class SList: # s 리스트 생성 하면서 노드 크래스 생성 노드 클래스가 slist 안에 들어가야댐 중첩 클래스:
    class Node:
        def __init__(self, item , link):  # node 클래스 멤버 함수
            self.item = item 
            self.next = link

    def __init__(self): # SList의 멤버 함수 # 생성자 counstrudct
            print("나는 SList의 Constructor method")
            self.head = None
            self.size = 0
    
    def isEmpty(self):
         return self.size == 0
    
    def insert_index(self, index, item):
      if index < 0 or index > self.size:
          print("인덱스 범위 초과")
          return None
      elif index == 0:
          self.insert_front(item)
      else:
          p = self.head
          for i in range(index - 1):
              p = p.next
          self.insert_after(item, p)
    
    def insert_front(self, item):
      if self.isEmpty():
        self.head = self.Node(item, None)
      else:
        self.head = self.Node(item, self.head)
      self.size += 1

    def insert_after(self,item,p):
      p.next = self.Node(item,p.next)
      self.size +=1

    def find(self, target):
      p = self.head # 100번지 헤드변수 에값을 p에 넣음
      #k = 0,1,2 k에들어감 
      for k in range(self.size):
        if target == p.item: # 타겟값 채리 p가 가리키는 노드 아이템값 체리
          return k # 거짓이면 수행안함 
        p = p.next

    def remove_front(self):
         if self.isEmpty():
          print("삭제 작업 불가")
          return None
         else:    
          temp = self.head
          self.head = self.head.next
          del temp
          self.size -= 1

    def remove_after(self, p):
      if self.isEmpty():
          print("리스트가 비어있어 삭제 불가")
          return None
      else:
        temp = p.next
        p.next = temp.next
        del temp
        self.size -= 1
    
    def delete_index(self, index):
      if index >= self.size:
          print("인덱스 범위 초과")
          return None
      elif index == 0:
          self.remove_front()
      else:
          p = self.head
          for i in range(index - 1):
              p = p.next
          self.remove_after(p)

    def delete_final(self):
      if self.isEmpty():
          print("삭제 작업 불가")
          return None
      else:
          p = self.head
          while p.next.next is not None:
              p = p.next
          del p.next
          p.next = None
          self.size -= 1

    def showList(self):
      p = self.head
      while p:
        if p.next is not None:
          print(p.item,"=>", end=" ")
        else:
          print(p.item)
        p = p.next

if __name__ == "__main__":
  s = SList() # self 100번지가 숨겨져 있음 셀프를 쓰면아댐
  # s.insert_front("mango")
  # s.insert_front("apple")
  # s.showList()
    # #  s.insert_after("cherry",s.head.next)
    #  s.showList()
    #  index = s.find("cherry")
    #  #print("cherry는 %d 번째 노드에 있음" % index)
    # #  print("cherry는 %d번째 노드에 있음" % #d 서식 지정자라 감싸줘야함 ( ) 
    # #            (s.find("cherry")+1) ) 
     
    #  s.remove_front()
    #  print("첫번째 노드인 apple을 삭제후")
    #  s.showList()
    #  s.insert_front("melon")
    #  s.remove_after(s.head)
    #  print("mango 노드 삭제 후")
    #  s.showList()

    # 실습과제를 위해 추가된 코드
  s.insert_front("kiwi")
  s.insert_front("strawberry")
  s.insert_front("grape")
  s.insert_front("peach")
  s.insert_front("banana")

  s.insert_index(2, "pear")
  s.delete_index(3)
  s.delete_final()
  s.showList()

