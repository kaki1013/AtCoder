L, R = map(int, input().split())
L -= 1
R -= 1
S = input()
if L != R:
    if L == 0:
        if R == len(S) - 1:
            S = S[::-1]
        else:
            S = S[R::-1] + S[R+1:]
    else:
        ans = ''
        if R == len(S) - 1:
            S = S[:L] + S[:L-1:-1]
        else:
            S = S[:L]+S[R:L-1:-1]+S[R+1:]
print(S)