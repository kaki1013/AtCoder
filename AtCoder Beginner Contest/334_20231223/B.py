# 실패
from math import ceil, floor

A, M, L, R = map(int, input().split())

L = (L-A)/M
R = (R-A)/M
L = ceil(L)
R = floor(R)

print(R-L+1)
