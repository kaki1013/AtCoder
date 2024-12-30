S, T = input().split()
l = len(S)

flag = False
for w in range(1, l):  # step
    if flag:
        break
    for c in range(1, w+1):  # start
        tmp = S[c-1::w]
        if tmp == T:
            flag = True
            break

print('Yes' if flag else 'No')