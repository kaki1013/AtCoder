# TLE : 큐로 방금 칠해진 칸의 인접 칸 후보만 확인하는 식으로..
from collections import deque

H, W = map(int, input().split())
S_ = [input() for _ in range(H)]


def is_in(i, j):
    return (0 <= i < H) and (0 <= j < W)


S = [[int(S_[i][j] == '#') for j in range(W)] for i in range(H)]
count = sum([sum(line) for line in S])

set_S = set()
for i in range(H):
    for j in range(W):
        if S[i][j] == 1:
            set_S.add((i, j))

# init
new_count = count
q = deque([])
for i in range(H):
    for j in range(W):
        if (i, j) in set_S:
            continue
        adj_1 = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = i + dx
            new_y = j + dy
            if is_in(new_x, new_y) and (new_x, new_y) in set_S:
                adj_1 += 1
        if adj_1 != 1:
            continue
        q.append((i, j))

nxt = set()
tmp = set()
while q:
    i, j = q.popleft()
    tmp = set()
    if (i, j) in set_S:
        continue

    adj_1 = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = i + dx
        new_y = j + dy
        if is_in(new_x, new_y) and (new_x, new_y) in set_S:
            adj_1 += 1
    if adj_1 != 1:
        continue

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = i + dx
        new_y = j + dy
        nxt.add((new_x, new_y))
    tmp.add((i, j))
    new_count += 1

q = deque(nxt)
set_S |= tmp

print(q)
print(set_S)
print(count)
# iter
while count != new_count:
    count = new_count
    new_q = deque([])

    while q:
        i, j = q.popleft()
        tmp = set()
        if (i, j) in set_S:
            continue

        adj_1 = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = i + dx
            new_y = j + dy
            if is_in(new_x, new_y) and (new_x, new_y) in set_S:
                adj_1 += 1
        if adj_1 != 1:
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = i + dx
            new_y = j + dy
            new_q.append((new_x, new_y))
        tmp.add((i, j))
        new_count += 1

    q = deque(set(new_q))
    set_S |= tmp

print(count)