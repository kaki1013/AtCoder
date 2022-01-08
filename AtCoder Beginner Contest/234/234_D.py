# BOJ 2075와 유사
import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
# heap의 길이는 K로 유지 for K번째로 큰 수 관리
heap = [P[i] for i in range(K)]
heapq.heapify(heap)
# 최소 힙이기 때문에 현재 루트 노드가 K번째로 큰 수(= 가장 큰 K개 중에서 가장 작은 작은 값)
print(heap[0])
for i in range(K, N):
    heapq.heappush(heap, P[i])
    # K번째 이하의 수는 pop
    heapq.heappop(heap)
    print(heap[0])