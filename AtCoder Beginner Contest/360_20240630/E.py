# 실패 : 논리는 맞음
N, K = map(int, input().split())
mod = 998244353

p = (N**2) % mod
for _ in range(K):
    tmp = p*(N**2-2*N+2)+(1-p)*2
    tmp %= mod

    p = tmp * pow(N**2, -1, mod)
    p %= mod

ans = p + pow(2, -1, mod)*(N+2)*(1-p)
print(ans % mod)