X, Y = map(int, input().split('.'))
if 0 <= Y < 3:
    print(f"{X}-")
elif 3 <= Y < 7:
    print(X)
elif 7 <= Y < 10:
    print(f"{X}+")
