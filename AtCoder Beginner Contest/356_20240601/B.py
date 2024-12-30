N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(M):
    A[i] *= -1

for _ in range(N):
    food = list(map(int, input().split()))
    for i in range(M):
        A[i] += food[i]

flag = True
for i in range(M):
    if A[i] < 0:
        flag = False
        break

print("Yes" if flag else "No")
