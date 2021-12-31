# 트리 dfs
import sys
sys.setrecursionlimit(3*10**5)  # 문제 상황에 따라서 조절


def DFS(graph, visited, now, vst_list):
    visited[now] = True
    vst_list.append(now)

    all_vst = True
    for nxt in graph[now]:
        if not visited[nxt]:
            all_vst = False

    if not all_vst:
        for dest in graph[now]:
            if not visited[dest]:
                DFS(graph, visited, dest, vst_list)
                vst_list.append(now)
    else:
        if now == 1:
            return vst_list
        else:
            return

    return vst_list


N = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    adj[A].append(B)
    adj[B].append(A)
for i in range(N+1):
    adj[i].sort()

visited = [False for _ in range(N+1)]
visited[0] = True

visit_list = DFS(adj, visited, 1, [])
print(*visit_list)
