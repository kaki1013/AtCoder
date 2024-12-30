# 실패
A, B, C, D = map(int, input().split())
# A, B, C, D = 1,1,4,4,


xx, yy = (C-A)//4, (D-B)//2
ans = 8 * min(xx, yy)
C -= 4*xx
D -= 2*yy
print(A, B, C, D)

def get_area(x, y):
    if (x+y) % 2:  # odd
        return 1
    if x == y:
        return 2
    return 0

coord2area = {(0,0):2, (0,1):1, (0,2):0, (0,3):1, (1,0):1, (1,1):2, (1,2):1, (1,3):0}

for x in range(A, C):
    for y in range(B, D):
        ans += coord2area[y%2, x%4]

print(ans)
# print(A, B, C, D)
