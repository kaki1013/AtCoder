N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = A+A
dp = [0]
for i in range(2*N):
    dp.append(dp[-1] + A[i])

moved = 0
for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        moved += cmd[1]
    elif cmd[0] == 2:
        l, r = cmd[1:]
        l = (l + moved) % N
        r = (r + moved) % N
        if l > r:
            r += N
        if l == 0:
            l = N
            r += N
        print(dp[r]-dp[l-1])