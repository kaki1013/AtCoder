N = int(input())
A = list(map(int, input().split()))

tmp = [a for a in A if a != -1]
n1 = len(tmp)
n2 = len(set(tmp))

if n1 == n2:
    print('Yes')

    new_elements = list(set(range(1, N+1)) - set(tmp))

    idx = 0
    idx_elements = 0
    while idx < N:
        if A[idx] == -1:
            A[idx] = new_elements[idx_elements]
            idx_elements += 1
        idx += 1
    print(*A)
else:
    print('No')
