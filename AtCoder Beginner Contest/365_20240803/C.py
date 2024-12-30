# 실패 : 이분탐색 맞음 but 이해 잘못함
"""
1 2 3 4

1 1 1 1
1 2 2 2
1 2 3 3
1 2 3 4

a1 a2 ... ak/ ak+1 ak+2 ... an
ak : a1 a2 ... ak/ ak ak .. ak
    -> a1+...+ak + ak*(n-k)

a0 a1 ... ak-1/ ak-1 ak-1 .. ak-1
    -> a0+...+ak-1 + ak-1*(n-k)
    -> dp[k] + a[k-1]*(n-k)
"""
import random
# N, M = map(int, input().split())
# A = sorted(list(map(int, input().split())))

# N, M = random.randint(1, 20), random.randint(1, 200)
# A = [random.randint(1, 20000) for i in range(N)]

N, M = 19, 182
A = [362, 906, 1014, 2000, 2145, 2656, 3132, 4293, 6430, 7894, 7959, 8141, 8276, 8507, 11108, 11928, 12927, 15731, 16863]
print(N, M)
print(A)

if sum(A) <= M:
    print('infinite')
else:
    dp = [0]
    for a in A:
        dp.append(a + dp[-1])
    # print(A)
    # print(dp)

    ans = -1
    max_ = -1
    for idx in range(N):
        tmp = dp[idx+1] + A[idx] * (N-idx-1)
        # print(idx, tmp, ans, max_)
        if max_ <= tmp <= M:
            ans = idx
            max_ = tmp

    if ans == -1:
        print(0)
    else:
        print(A[ans])


# TEST
if sum(A) <= M:
    print("infinite")
    exit()

def cond(x):
    s = sum(min(x, a) for a in A)
    return s <= M

ok, ng = 0, max(A)

while ok + 1 < ng:
    mi = (ok + ng) // 2
    if cond(mi):
        ok = mi
    else:
        ng = mi

print(ok)