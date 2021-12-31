# 경로의 개수 구해서 합의 법칙 적용
# https://atcoder.jp/contests/abc211/editorial/2330
from collections import deque
import sys


def bfs(adj, vst, start):
    least_dist_list = [0] * (N + 1)

    q = deque([(start, 0)])   # 정점, 거리
    how_many = [0] * (N + 1)  # 최단경로의 수
    depth_count = [0] * (N + 1)  # 거리(깊이)가 i인 것들의 개수
    depth_count[0] = 1
    vst[start] = True

    for i in range(N+1):
        if vst[N]:
            break
        for j in range(depth_count[i]):
            curr, dist = q.popleft()
            for nxt in adj[curr]:
                if not vst[nxt] or dist + 1 == least_dist_list[nxt]:
                    if not vst[nxt]:
                        q.append((nxt, dist + 1))

                    how_many[nxt] += 1
                    depth_count[i+1] += 1
                    least_dist_list[nxt] = dist + 1
                    vst[nxt] = True

    return how_many


N, M = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    adj[A].append(B)
    adj[B].append(A)
visited = [False] * (N+1)

q = bfs(adj, visited, 1)
print(q)
"""
count = 0
for v, _ in q:
    if v == N:
        count += 1
print(count)
"""