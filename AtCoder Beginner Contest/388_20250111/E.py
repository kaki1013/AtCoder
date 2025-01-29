# 이분 매칭(Bipartite Matching)?
from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
selected = [False] * N

ans = 0
for a in A:
    idx = bisect_left(A, a*2)
    print(a, idx)
    # ans += bisect_right(A, a/2)

print(ans)
