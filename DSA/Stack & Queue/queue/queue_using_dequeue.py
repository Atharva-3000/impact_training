from collections import deque
s=deque()
s.append(10)
s.append(20)
s.append(30)
print(*s)
s.popleft()
print(*s)