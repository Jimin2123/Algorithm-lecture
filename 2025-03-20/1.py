list = [10,20,30]
print(f'기존값: {list}')
list.append(40)
print(f'기존값: {list}')
#a = list.pop()
#a = list.pop(len(list) - 1)
a = list.pop(-1)
print(f'기존값: {list}')
print('꺼낸값: %d' % a)