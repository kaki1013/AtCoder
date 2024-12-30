N, L, R = map(int, input().split())
arr = [i+1 for i in range(N)]

L -= 1
R -= 1
arr[L:R+1] = arr[R:L-1:-1] if L != 0 else arr[R::-1]

print(*arr)