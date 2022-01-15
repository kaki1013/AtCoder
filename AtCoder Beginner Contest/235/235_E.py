"""
MST 찾고, 쿼리로 주어진 간선 (u, v, w)에 대해
가중치가 w 보다 작은 MST의 간선들(최대 N-1개)로 이루어진 그래프에서 u와 v가 다른 연결요소에 속하면 Yes, 아니면 No
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    p[a] = b

n, m, q = map(int, input().split())
p = [i for i in range(n)]
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))

# Kruskal's algorithm
edges.sort()
count = 0
MST = []
for w, u, v in edges:
    a, b = find(u), find(v)
    if a != b:
        union(a, b)
        MST.append((w, u, v, -1))
        count += 1
    if count == n-1:
        break

# MST에 함께 넣고 그 당시에 쿼리의 간선이 선택 됐을지 확인 for 시간복잡도 O((N+Q)log(N+Q))
for i in range(q):
    u, v, w = map(int, input().split())
    MST.append((w, u-1, v-1, i))
MST.sort()

ans = [''] * q
p = [i for i in range(n)]
for w, u, v, is_query in MST:
    if is_query == -1:
        union(find(u), find(v))
    else:
        ans[is_query] = 'Yes' if find(u) != find(v) else 'No'
for a in ans:
    print(a)