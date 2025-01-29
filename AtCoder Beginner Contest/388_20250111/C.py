from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += bisect_right(A, a/2)

print(ans)
