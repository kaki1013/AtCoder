"""
4
0 10
0 10
0 10
-30 -29

4
-10 0
-10 0
-10 0
29 30

"""
N = int(input())
LRs = [tuple(map(int, input().split())) for i in range(N)]

l, r = 0, 0
for i in range(N):
    a, b = LRs[i]
    l += a
    r += b

flag = (l <= 0) and (r >= 0)
if flag:
    ans = [LRs[i][1] for i in range(N)]  # init : largest
    goal = sum(ans)  # desc r

    for i in range(N):
        # print(i, goal, ans)
        if goal == 0:
            break

        l, r = LRs[i]
        if goal > r-l:  # possible desc
            ans[i] = l
            goal -= r-l
        else:  # goal <= r-l
            ans[i] -= goal
            goal = 0

    print('Yes')
    print(*ans)
else:
    print('No')
