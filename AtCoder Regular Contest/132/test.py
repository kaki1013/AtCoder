import random
from collections import deque

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = deque(l)

for i in range(int(random.random() * 10000000 // 1000)):
    r = random.randint(1, 3)
    if r == 1:
        l.appendleft(l.pop())
    if r == 2:
        l.append(l.popleft())
    if r == 3:
        l.reverse()
    print(r, l)