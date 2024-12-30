# 실패
from bisect import bisect_left, bisect_right

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))
X.sort()

l, r = [], []
for i in range(N):
    if S[i] == '0':  # left
        l.append(X[i])
    else:  # '1': right
        r.append(X[i])

# print(l)
ans = 0
for x in r:
    # # j s.t. x_i < x_j <= x_i + 2*t
    idx1 = bisect_left(l, x)
    idx2 = bisect_right(l, x+2*T)
    # print(idx1, idx2)
    ans += idx2-idx1
print(ans)
