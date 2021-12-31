N, X = map(int, input().split())
A = [0]
for i in tuple(map(int, input().split())):
    A.append(i)
ans = 1

visited = [False] * (N+1)
visited[X] = True

curr = X
while True:
    if not visited[A[curr]]:
        curr = A[curr]
        visited[curr] = True
        ans += 1
    else:
        break
print(ans)
