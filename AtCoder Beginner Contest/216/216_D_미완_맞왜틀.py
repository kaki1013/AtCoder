from collections import deque
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cylinders = []
for _ in range(M):
    k = int(sys.stdin.readline().rstrip())
    cylinder = deque(map(int, sys.stdin.readline().rstrip().split()))  # 위 -> 아래 순
    cylinders.append(cylinder)

achievable = False
while True:
    popped = False
    if cylinders == [deque([]) for _ in range(M)]:
        achievable = True
        break
    seen = dict()
    for i in range(M):
        cylinder = cylinders[i]
        if not cylinder:
            continue
        top = cylinder[0]
        if top not in seen:
            seen[top] = i
        else:
            previous_idx = seen[top]
            cylinders[previous_idx].popleft()
            cylinders[i].popleft()
            popped = True
            break
    if not popped:  # pop 없이 순회를 완료한 상황
        break

print("Yes" if achievable else "No")

"""
예시:
4 3
3
4 2 1
3
3 4 2
2
3 1

[[1, 2, 4], [2, 4, 3], [1, 3]]
"""