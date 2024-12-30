from bisect import bisect_right

N = int(input())
p = [list(map(int, input().split())) for i in range(N)]
p.sort()

l = [l for l, r in p]

ans = 0
for i in range(N):
    x = p[i][1]
    idx = bisect_right(l, x)
    # print(x, idx-i-1)
    ans += idx-i-1

print(ans)
