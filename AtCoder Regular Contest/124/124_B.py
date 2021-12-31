N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

possible = []

dp = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        dp[i][j] = a[i] ^ b[j]

for i in range(N):
    check = dp[0][i]
    have_check = True
    for j in range(1, N):
        if check not in dp[j]:
            have_check = False
            break
    if have_check:
        possible.append(check)

possible = list(set(possible))

print(len(possible))
for i in sorted(possible):
    print(i)