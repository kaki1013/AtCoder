# 2*total_weight - diameter
import sys

input = sys.stdin.readline
sys.setrecursionlimit(3 * 10 ** 5)


def DFS(gragh, visited, start, dist):
    if visited[start]:
        return
    visited[start] = True
    for adj, w in gragh[start]:
        if not visited[adj]:
            dist[adj] = dist[start] + w
            DFS(gragh, visited, adj, dist)


n = int(input())
tree = [[] for _ in range(n + 1)]
total_weight = 0
for _ in range(n - 1):
    x, y, weight = map(int, input().split())
    tree[x].append([y, weight])
    tree[y].append([x, weight])
    total_weight += weight

visited = [False] * (n + 1)
dist = [0] * (n + 1)

DFS(tree, visited, 1, dist)
Max_where, Max_dist = 1, 0
for i in range(1, n + 1):
    if dist[i] > Max_dist:
        Max_where = i
        Max_dist = dist[i]

visited = [False] * (n + 1)
dist = [0] * (n + 1)

DFS(tree, visited, Max_where, dist)
Max_where, Max_dist = 1, 0
for i in range(1, n + 1):
    if dist[i] > Max_dist:
        Max_where = i
        Max_dist = dist[i]

print(2 * total_weight - Max_dist)
