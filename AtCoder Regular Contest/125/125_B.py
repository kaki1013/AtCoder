# 실패
from math import floor
N = int(input())
root = int(N**0.5)
mod = 998244353
ans = N * (N + 1) // 2
ans %= mod

for i in range(int(root)+1, N+1):
    ans += floor(-(i*i-N)**0.5)
    ans %= mod

print(ans)
