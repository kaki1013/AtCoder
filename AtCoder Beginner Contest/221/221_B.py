S = input()
T = input()
l = len(S)
similar = bool(S==T)
if S != T:
    same, change = 0, 0
    for i in range(l):
        if S[i] == T[i]:
            same += 1
        elif i < l-1:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                change += 2
    similar = bool(same + change == l and change == 2)
print('Yes' if similar else 'No')
