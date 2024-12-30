from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

d = dict()
for i in range(N):
    for j in range(i+1, N):
        diff = A[j]-A[i]
        if diff in d:
            d[diff].append((i, j))
        else:
            d[diff] = [(i, j)]

ans = [0]*N
ans[0] = N

# process
for arr in d.values():
    fst, snd = zip(*arr)  # for bisect
    arr_len = len(arr)

    stack = [(i, 2) for i in range(arr_len)]
    while stack:
        curr, length = stack.pop()
        ans[length-1] += 1
        l, r = arr[curr]

        nxt_idx = bisect_left(fst, r)
        if nxt_idx >= arr_len:
            nxt_idx -= 1

        is_equal = True
        for nxt in range(nxt_idx, arr_len):
            ll, rr = arr[nxt]
            is_equal = (r == ll)

            if not is_equal:
                break

            if r == ll:
                stack.append((nxt, length+1))
            else:
                is_equal = False

print(*ans)
