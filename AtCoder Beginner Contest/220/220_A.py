A, B, C = map(int, input().split())
m = A // C
ans = -1
if A <= C * m <= B:
    ans = C * m
if A <= C * (m+1) <= B:
    ans = (m + 1) * C
print(ans)
