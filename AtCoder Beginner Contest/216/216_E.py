N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
count = dict()
for i in range(N):
    a = A[i]
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

ans = 0
if sum(A) <= K:
    for i in range(N):
        a = A[i]
        ans += a*(a+1)//2
else:
    max_satisfaction = A[-1]
    while K != 0:
        max_count = count[max_satisfaction]
        if A[0] == max_satisfaction:  # ex: 100 100 ... 100
            how_many = K // N
            K -= how_many * N
            temp = (max_satisfaction*(max_satisfaction+1)//2 - (max_satisfaction-how_many)*(max_satisfaction-how_many+1)//2)
            ans += temp * N
            max_satisfaction -= how_many

            ans += max_satisfaction * K
            K = 0
        else:
            second_max = A[-1-max_count]
            diff = max_satisfaction - second_max
            if diff * max_count > K:
                how_many, r = K // max_count, K % max_count
                K -= how_many * max_count
                temp = (max_satisfaction * (max_satisfaction + 1) // 2 - (max_satisfaction - how_many) * (max_satisfaction - how_many + 1) // 2)
                ans += temp * max_count
                if max_satisfaction-how_many not in count:
                    count[max_satisfaction-how_many] = 0
                max_satisfaction -= how_many
                count[max_satisfaction] += max_count

                ans += max_satisfaction * r
                K -= r
            else:
                K -= diff * max_count
                mstf, scdm = max_satisfaction, second_max
                ans += (mstf*(mstf+1)//2 - scdm*(scdm+1)//2) * max_count
                count[second_max] += count[max_satisfaction]
                count[max_satisfaction] = 0
                max_satisfaction = second_max
print(ans)
