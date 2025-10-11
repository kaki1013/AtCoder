# ans = M - # max edges for retaining bipartite graph
N, M = map(int, input().split())
# adj = [[] for _ in range(N)]
# for _ in range(M):
#     u, v = map(int, input().split())
#     adj[u-1].append(v-1)
#     adj[v-1].append(u-1)
uv = []
for _ in range(M):
    u, v = map(int, input().split())
    uv.append((u-1, v-1))

max_edges = 0
for party in range(1 << N):
    edges_count = 0
    for u, v in uv:
        u_party = party & (1 << u)
        v_party = party & (1 << v)
        if (u_party == v_party == 0) or (u_party != 0 and v_party != 0):  # don't need this edge
            continue
        edges_count += 1
    max_edges = max(max_edges, edges_count)

print(M - max_edges)