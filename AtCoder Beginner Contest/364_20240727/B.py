H, W = map(int, input().split())
r, c = map(int, input().split())
r-=1
c-=1
board = [list(input()) for _ in range(H)]
X = input()

direction = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

for char in X:
    dc, dr = direction[char]
    rr, cc = r+dr, c+dc
    if 0 <= rr < H and 0 <= cc < W and board[rr][cc] == '.':
        r = rr
        c = cc
print(r+1, c+1)