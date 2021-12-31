N, X = map(int, input().split())
L = []
for _ in range(N):
    __, *A = map(int, input().split())
    L.append(A)

count = 0
def dfs(idx, goal):
    global count
    if idx == N:
        if goal == 1:
            count += 1
        return
    for a in L[idx]:
        if goal % a:
            continue
        dfs(idx + 1, goal // a)

dfs(0, X)
print(count)
