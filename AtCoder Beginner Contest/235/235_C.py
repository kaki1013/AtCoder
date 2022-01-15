import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
count = dict()
for i in range(N):
    a = A[i]
    if a in count:
        count[a][0] += 1
        count[a][1].append(i)
    else:
        count[a] = [1, [i]]     # number, [idx]
for _ in range(Q):
    x, k = map(int, input().split())
    if x not in count:
        print(-1)
        continue
    n = count[x][0]
    if n < k:
        print(-1)
    else:
        print(count[x][1][k-1] + 1)