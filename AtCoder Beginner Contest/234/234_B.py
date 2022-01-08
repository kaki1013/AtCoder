N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
ans_square = 0
for i in range(N):
    x1, y1 = points[i]
    for j in range(i+1, N):
        x2, y2 = points[j]
        temp = (x1-x2)**2 + (y1-y2)**2
        ans_square = max(ans_square, temp)
print(ans_square**0.5)