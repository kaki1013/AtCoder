# 실패
"""
https://atcoder.jp/contests/abc364/editorial/10559

knapsack dp?
dp[i][j] == (i번째 아이템까지 살펴봤을 때, 배낭의 최대 무게가 j일 때의 최대 가치)
dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])
"""
N, X, Y = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * 10001 for _ in range(N)]
print(AB)