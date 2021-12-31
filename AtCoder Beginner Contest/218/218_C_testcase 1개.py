"""
O(N^2)
T의 # 추출 후 S에 존재하는지 체크, 4방향 최전하면서 체크
"""


def rotate(grid, M, N):
    rotated = []
    for i in range(N):
        temp = []
        for j in range(M-1, -1, -1):
            temp.append(grid[j][i])
        rotated.append(''.join(temp))
    return rotated


N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


top, bot, left, right = 0, 0, 0, 0
breaker = False
for row in range(N):
    if breaker:
        break
    for col in range(N):
        if T[row][col] == '#':
            top, bot, left, right = row, row, col, col
            breaker = True
            break

for row in range(N):
    for col in range(N):
        if T[row][col] == '#':
            top = min(top, row)
            bot = max(bot, row)
            left = min(left, col)
            right = max(right, col)

sub_grid = [T[row][left:right+1] for row in range(top, bot+1)]
m, n = bot - top + 1, right - left + 1

makable = False
for _ in range(4):
    if makable:
        break
    sub_grid = rotate(sub_grid, m, n)
    m, n = n, m
    for row in range(N-m+1):
        if makable:
            break
        for col in range(N-n+1):
            compare = []
            for i in range(m):
                temp = []
                for j in range(n):
                    temp.append(S[row+i][col+j])
                compare.append(''.join(temp))
            if sub_grid == compare:
                makable = True
                break
print('Yes' if makable else 'No')
