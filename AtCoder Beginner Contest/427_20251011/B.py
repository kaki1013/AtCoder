N = int(input())

def f(n):
    s = str(n)
    tmp = 0
    for c in s:
        tmp += int(c)
    return tmp

A = [1]
dp = [1]

for _ in range(N-1):
    A.append(f(dp[-1]))
    dp.append(dp[-1] + A[-1])

print(dp[-1])
