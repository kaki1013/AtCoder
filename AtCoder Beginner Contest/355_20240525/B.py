N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)

s = set(A)
a = []
for i in range(N+M):
    if C[i] in s:
        a.append(i)

flag = False
for i in range(N-1):
    if abs(a[i] - a[i+1]) == 1:
        flag = True
        break
print('Yes' if flag else 'No')
