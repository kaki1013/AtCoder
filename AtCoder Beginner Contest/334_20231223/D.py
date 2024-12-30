"""
i<j 라면 Q[i]<Q[j]
파라메트릭 서치? O(Q logN)

S개의 썰매를 끄는 최소의 루돌프 마리수 R
S : 1~N

"""
from bisect import bisect_right
N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

R_sum = [R[0]]
for i in range(1, N):
    R_sum.append(R_sum[-1] + R[i])

for _ in range(Q):
    query = int(input())
    ans = bisect_right(R_sum, query)
    print(ans)
