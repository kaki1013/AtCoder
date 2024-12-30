N, T = map(int, input().split())
A = list(map(int, input().split()))

def get_ij(x):
    i, j = x//N+1, x%N
    if j == 0:
        i -= 1
        j = N
    return i, j

rows = [0] * N
cols = [0] * N
diag = [0] * 2  # i==j or i+j==N+1

flag = False
for idx in range(T):
    i, j = get_ij(A[idx])

    rows[i-1] += 1
    cols[j-1] += 1
    if i == j:
        diag[0] += 1
    if i+j == N+1:
        diag[1] += 1

    if N in rows or N in cols or N in diag:
        flag = True
        print(idx+1)
        break

if not flag:
    print(-1)
