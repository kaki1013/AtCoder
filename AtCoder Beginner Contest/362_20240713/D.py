import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

# weight := 가중치 인접 리스트 (from u to v)
weight = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, b = map(int, input().split())
    weight[u].append((v, b))
    weight[v].append((u, b))

priority_queue = []
distance = [10**16 for _ in range(N+1)]
found = [False for _ in range(N+1)]

distance[1] = A[0]
heapq.heappush(priority_queue, (A[0], 1))  # (거리, 정점 번호)

while priority_queue:
    _, u = heapq.heappop(priority_queue)
    if found[u]:
        continue
    found[u] = True
    for v, w in weight[u]:
        if distance[v] > distance[u] + w + A[v-1]:
            distance[v] = distance[u] + w + A[v-1]
            heapq.heappush(priority_queue, (distance[v], v))

ans = distance[2:]
print(*ans)
