N = int(input())
print("Yes" if len(set([input() for _ in range(N)])) != N else "No")
