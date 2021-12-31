# sol1: 오류 O
# 최선: 나 + 300 // 최악 : 나 - 300 ( <=> 타인 + 300)
# 최선과 최악일 때 등수는 이진탐색으로 계산
"""
def bisect(arr, v, size):   # v '이상'인 데이터의 개수 반한
    if v >= arr[0]: return 1
    if v < arr[size-1]: return size
    l, r = 0, size
    while True:
        if l == r: return l
"""
from bisect import bisect

N, K = map(int, input().split())
P = sorted([(sum(tuple(map(int, input().split()))), i+1) for i in range(N)])
P_value = [P[i][0] for i in range(N)]
result = [False] * N

for i in range(N):
    value, idx = P[i]
    best = N - bisect(P_value, value + 300) + 1
    worst = N - bisect(P_value, value - 300)
#    print(best, worst)
    if best <= K <= worst:
        result[idx-1] = True

for i in range(N):
    print('Yes' if result[i] else 'No')

# sol2:
n, k = map(int, input().split())
s = [0] * n
for i in range(n):
    s[i] = sum(map(int, input().split()))
t = sorted(s, reverse=True)[k - 1]
for x in s:
    print("Yes" if x + 300 >= t else "No")
