candidate = []
for length in range(3, 10+1):
    # d = 0
    for i in range(1, 10):
        num = int(str(i) * length)
        candidate.append(num)
    # d > 0
    for d in range(1, (9-1)//(length-1)+1):     # 1..9
        for start in range(1, 9-(length-1)*d + 1):
            temp = [str(start + d * i) for i in range(length)]
            num = int(''.join(temp))
            candidate.append(num)
    # d < 0
    for d in range(1, (9-0)//(length-1)+1):     # 9..0
        for start in range(9, (length-1)*d-1, -1):
            dd = -d
            temp = [str(start + dd * i) for i in range(length)]
            num = int(''.join(temp))
            candidate.append(num)
for length in range(11, 18+1):
    # d = 0
    for i in range(1, 10):
        num = int(str(i) * length)
        candidate.append(num)
candidate.sort()

X = input()
N = int(X)
if len(X) > 2:
    for num in candidate:
        if num >= N:
            ans = num
            break
else:
    ans = X
print(ans)
