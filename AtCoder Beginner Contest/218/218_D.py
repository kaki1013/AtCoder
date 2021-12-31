N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]
xy_set = set(xy)
ans = 0
for i in range(N):
    for j in range(i, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if x1 == x2 or y1 == y2:
            continue
        if (x1, y2) in xy_set and (x2, y1) in xy_set:
            ans += 1
ans //= 2
print(ans)
