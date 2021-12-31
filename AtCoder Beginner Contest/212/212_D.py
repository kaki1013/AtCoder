import sys
import heapq

heap = []
heapq.heapify(heap)

Q = int(sys.stdin.readline().rstrip())
minus = 0
for _ in range(Q):
    query = sys.stdin.readline().rstrip().split()
    if len(query) == 2:
        X = int(query[1])
        if query[0] == '1':
            heapq.heappush(heap, X-minus)  # minus 만큼 누적된 차이만큼 빼서 저장
        if query[0] == '2':
            minus += X  # 기존에 있던 수들에 X를 더하는 것 == 앞으로 들어올 수들에서 X를 빼는 것
    else:
        num = heapq.heappop(heap)  # A + X < B <=> A < B - X 이므로 최소원소 구하는 것과 무관
        print(num + minus)  # 뺀 만큼 더해주어야 함
