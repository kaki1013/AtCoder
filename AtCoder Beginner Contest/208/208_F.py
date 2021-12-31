def solve(dp, n, m):
    if dp[m][n] != -1:
        return dp[m][n]
    if dp[m-1][n] != -1 and dp[m][n-1] != -1:
        dp[m][n] = (dp[m-1][n] + dp[m][n-1]) % (10**9+7)
        return dp[m][n]
    else:
        dp[m-1][n] = solve(dp, n, m-1)
        dp[m][n-1] = solve(dp, n-1, m)
        dp[m][n] = (dp[m-1][n] + dp[m][n-1]) % (10**9+7)
        return dp[m][n]


N, M, K = map(int, input().split())
dp = [[-1] * (N+1) for _ in range(M+1)]
dp[0] = [i ** K for i in range(N+1)]
for m in range(M+1):
    dp[m][0] = 0

print(solve(dp, N, M))