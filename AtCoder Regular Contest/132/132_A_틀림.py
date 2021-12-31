# 틀림: https://atcoder.jp/contests/arc132/editorial/3199
# 0 . // 1 #
import sys
input = sys.stdin.readline

n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))
r_pos = [0 for _ in range(n+1)]
c_pos = [0 for _ in range(n+1)]
for i in range(n):
    r_pos[R[i]] = i
    c_pos[C[i]] = i

board = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(1, n+1):
    if i % 2:  # odd
        goal = n + 1 - (i + 1) // 2
        goal_r = r_pos[goal]
        goal_c = c_pos[goal]
        for j in range(n):
            if board[goal_r][j] == -1:
                board[goal_r][j] = 1
            if board[j][goal_c] == -1:
                board[j][goal_c] = 1
    else:  # even
        goal = i // 2
        goal_r = r_pos[goal]
        goal_c = c_pos[goal]
        for j in range(n):
            if board[goal_r][j] == -1:
                board[goal_r][j] = 0
            if board[j][goal_c] == -1:
                board[j][goal_c] = 0

tr = {0: '.', 1: '#'}
ans = ''
q = int(input())
for _ in range(q):
    r, c = map(int, input().split())
    ans += tr[board[r-1][c-1]]
print(ans)
