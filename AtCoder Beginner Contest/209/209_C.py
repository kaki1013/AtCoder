"""
from collections import deque

N = int(input())
Cs = list(map(int, input().split()))
mod = 10 ** 9 + 7

q = deque([[[], 0, set()]])

while q and q[0][1] != N:
    data = q.popleft()  # 처음은 [[], 0]
    for j in range(1, Cs[data[1] - 1] + 1):
        seq, count, used = data[0][:], data[1], set(data[2])
        if j not in used:
            seq.append(j)
            count += 1
            used.add(j)
            q.append([seq, count, used])

print(len(q) % mod)
"""
N = int(input())
Cs = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7
ans = 1
for i in range(N):
    ans = (ans * (Cs[i] - i)) % mod
print(ans)