N = int(input())
A = list(map(int, input().split()))
X = int(input())

dp_sum = [0]
for i in range(N):
    dp_sum.append(dp_sum[-1] + A[i])

ans = 0
ans += ((X // dp_sum[-1]) * N)
X %= dp_sum[-1]

if X:
    for i in range(1, N+1):
        if dp_sum[i] > X:
            ans += i
            break
else:
    ans += 1

print(ans)
