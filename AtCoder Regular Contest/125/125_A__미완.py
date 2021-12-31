# 반례 있음
N, M = map(int, input().split())
S, T = input().split(), input().split()

ans = -1
if T == ['0'] * M:
    if S != ['1'] * N:
        left, right = 0, 1
        while S[left] != '0':
            left += 1
        while S[-right] != '0':
            right += 1
        ans = min(left, right) + M
elif T == ['1'] * M:
    if S != ['0'] * N:
        left, right = 0, 1
        while S[left] != '1':
            left += 1
        while S[-right] != '1':
            right += 1
        ans = min(left, right) + M
else:
    if not (S == ['0'] * N or S == ['1'] * N):
        start, end = 0, N - 1
        left, right = 0, 1
        while S[(start + left) % N] == S[(end + left) % N]:
            left += 1
        while S[(start - right) % N] == S[(end - right) % N]:
            right += 1
        if left < right:
            ans = left
            move_start = left
        elif left > right:
            ans = right
            move_start = (-right + N) % N
        else:
            if S[left] == T[0]:
                ans = left
                move_start = left
            elif S[(-right + N) % N] == T[0]:
                ans = right
                move_start = (-right + N) % N
            else:
                ans = left + 1
                move_start = (left - 1 + N) % N
                S[move_start] = T[0]

        if S[move_start] != T[0]:
            ans += 1

        state, change = T[0], 0
        for char in T:
            if state != char:
                change += 1
                state = char
        ans += change
        ans += M

print(ans)

"""
9 9
0 0 1 1 0 1 0 1 0
0 1 0 0 1 0 1 0 0
"""