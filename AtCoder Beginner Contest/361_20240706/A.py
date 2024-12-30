N, K, X = map(int, input().split())
A = list(map(int, input().split()))
ans = A[:K]+[X]+A[K:]
print(*ans)