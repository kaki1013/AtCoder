# 실패
from collections import deque
N = int(input())
S = list(input())+['', '']
T = list(input())+['', '']

ans = -1
if sum([1 if S[i] == 'B' else 0 for i in range(N)]) == sum([1 if T[i] == 'B' else 0 for i in range(N)]):

    q = deque([[S, 0, N]])  # state, count, empty_index
    vst = set()
    vst.add((tuple(S)))
    while q:
        curr, count, empty = q.popleft()
        if curr == T:
            ans = count
            break

        tmp = curr
        for i in range(N+1):
            if i+1 == empty or i == empty or i == empty+1:
                continue
            tmp[i], tmp[i+1], tmp[empty], tmp[empty+1] = tmp[empty], tmp[empty+1], tmp[i], tmp[i+1]

            if tuple(tmp) in vst:
                continue
            q.append([tmp[:], count+1, i])
            tmp[i], tmp[i+1], tmp[empty], tmp[empty+1] = tmp[empty], tmp[empty+1], tmp[i], tmp[i+1]
            # print(q)

print(ans)
