import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
mod = 998244353
restrictions = [sys.stdin.readline().rstrip().split() for _ in range(K)]
case_number = [K] * N
have_must_number = [False] * N

for i in range(K):
    c, k = restrictions[i][0], int(restrictions[i][1]) - 1

    have_must_number[k] = True
    if c == 'L':
        for j in range(k):
            case_number[j] -= 1
    elif c == 'R':
        for j in range(k+1, N):
            case_number[j] -= 1

ans = 1
for i in range(N):
    if not have_must_number[i]:
        ans = (ans * case_number[i]) % mod
print(ans)
