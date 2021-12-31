# N개의 정점과 N-1개의 간선 & 한 지점에서 다른 지점으로 가는 경로가 반드시 존재 => 트리
from collections import deque
from sys import stdin
input = stdin.readline


def bfs(adj, vst, blackwhite):
    q = deque([(1, 1)])
    vst[1] = True
    blackwhite[1] = 1

    while q:
        curr, dist = q.popleft()
        for nxt in adj[curr]:
            if not vst[nxt]:
                q.append((nxt, dist+1))
                vst[nxt] = True
                blackwhite[nxt] = (dist + 1) % 2


# c에서 d가 같은 색(검정, 하양) 이면 타운, 아니면 로드
N, Q = map(int, input().rstrip().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)
BlackWithe = [None] * (N+1)
visited = [False] * (N + 1)

bfs(adj, visited, BlackWithe)

queries = [tuple(map(int, input().rstrip().split())) for _ in range(Q)]
for query in queries:
    a, b = query[0], query[1]
    if BlackWithe[a] == BlackWithe[b]:
        print('Town')
    else:
        print('Road')
