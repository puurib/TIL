#
from collections import deque
from collections import deque

deq = deque([1,2,3,4,5])

deq.append(6)
#기존 append는 맨 뒤에 넣기만 가능하나 appendleft() 맨 왼쪽 넣기도 가능 (O(1))
print(deq)                          # deque([1, 2, 3, 4, 5, 6])
deq.appendleft(0)
print(deq)                          # deque([0, 1, 2, 3, 4, 5, 6])
deq.pop()
print(deq)                          # deque([0, 1, 2, 3, 4, 5])
#기존 pop은 맨 뒤에꺼 제거만 가능. popleft() 맨 왼쪽꺼 제거 가능 (O(1))
deq.popleft()
print(deq)                          # deque([1, 2, 3, 4, 5])



