N, K = map(int, input().split())
arr = list(map(int, input().split()))

get = [0] * N
sort_arr = sorted(arr)
how_small = dict()
for i in range(N):
    how_small[i+1] = sort_arr[i]
index = dict()
for i in range(N):
    index[arr[i]] = i

while True:
    if K >= N:
        get = [K // N] * N
        K %= N
    else:
        for i in range(K):
            get[index[how_small[i+1]]] += 1
        break

for num in get:
    print(num)