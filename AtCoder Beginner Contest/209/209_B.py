N, X = map(int, input().split())
prices = list(map(int, input().split()))

for i in range(N):
    if i % 2 == 1:
        prices[i] -= 1

s = sum(prices)
if X >= s:
    print('Yes')
else:
    print('No')