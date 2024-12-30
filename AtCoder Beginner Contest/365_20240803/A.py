Y = int(input())
if Y % 4 != 0:
    ans = 365
else:
    if Y % 100 != 0:
        ans = 366
    else:
        if Y % 400 != 0:
            ans = 365
        else:
            ans = 366
print(ans)
