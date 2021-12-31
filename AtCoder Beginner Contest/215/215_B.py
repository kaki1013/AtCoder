N = int(input())
i = 0
while 2 ** (i+1) <= N:
    i += 1
print(i)
