# 실패
N, K = map(int, input().split())
A = list(map(int, input().split()))

diff = [A[i+1]-A[i] for i in range(K-1)]
diff.sort()

ans = A[-1] - A[0]
for i in range(K-1-K//2):
    tmp = diff.pop()
    ans -= tmp
print(ans)