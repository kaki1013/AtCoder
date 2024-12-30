N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

"""
0 1 2 ... N-1

0 1 2 ... N-K-1
1 2 ... N-K
...

i ... N-K-1+i
...
K...N-1
"""

tmp = A[N-K-1]-A[0]
for i in range(1, K+1):
    tmp = min(tmp, A[N-K-1+i]-A[i])
print(tmp)