N = int(input())
A = list(map(int, input().split()))
mod = 998244353

count = [0 for _ in range(10)]
count[(A[0] + A[1]) % 10] += 1
count[(A[0] * A[1]) % 10] += 1

for n in range(2, N):
    F = [0 for _ in range(10)]
    G = [0 for _ in range(10)]
    now = A[n]
    for i in range(10):
        F[(i + now) % 10] += count[i]
        G[(i * now) % 10] += count[i]
    for i in range(10):
        count[i] = (F[i] + G[i]) % mod

for c in count:
    print(c)
