N, K = map(int, input().split())
A = list(map(int, input().split()))

cul_sum = [0]
for a in A:
    cul_sum.append(cul_sum[-1] + a)
sum_set = set(cul_sum)

count = 0
for i in range(1, N+1):
    now = cul_sum[i]
    if now - K in sum_set:
        for j in range(i):
            if now - K == cul_sum[j]:
                count += 1
print(count)