N, M = map(int, input().split())
mod = 998244353
bit = 60

count = 0

for i in range(60):
    if M & (1 << i):
        count += (N // 2**(i+1)) * 2**i
        if N % (2**(i+1)) >= 2**i:
            count += N % (2**i)
            count += 1
    count %= mod

print(count)
