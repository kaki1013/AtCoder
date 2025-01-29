# """
# 5 	0 	9 	3
# 0
# -1 	+1
# -1	-1	+2
# -1	0	-1	+1
#
# 1 베이스
#
# 5는 4-1=3 이상		= 2
# // (5>=3) 다음 사람 3명 전체 -> 1+3=4번까지
#
# 0+ 3/3 = 1은 4-2=2보다 작음	= 0
# // (1 < 2) 다음 사람 2-1=1명 -> 2+1=3번까지
#
# 9 + 1 + 1 = 11 은 4-3=1보다 큼	= 10
# // (11 >= 1) 다음 사람 1명 전체 -> 3+1=4번까지
#
# 3 + 1 + 0 + 1 			= 5
# // (5 >= 0) 다음 사람 없음
# """
# def initialize(index, start, end):
#     if start == end:
#         nodes[index] = original[start]
#         return nodes[index]
#     mid = (start + end) // 2
#     left = initialize(index * 2, start, mid)
#     right = initialize(index * 2 + 1, mid + 1, end)
#     nodes[index] = left + right     # min(left, right), max(left, rigtt) 등으로 변형 가능
#     return nodes[index]
#
#
# # 해당 index의 노드가 커버(포함)하는 구간 [nodeStart, nodeEnd]과 질의하는 구간 [reqStart, reqEnd]
# def query(index, nodeStart, nodeEnd, reqStart, reqEnd):
#     nodeMid = (nodeStart + nodeEnd) // 2
#     if reqEnd < nodeStart or nodeEnd < reqStart:
#         return 0                    # min은 INF, max는 -INF 등 '영향을 주지 않는 값'으로 변형 가능
#     elif reqStart <= nodeStart and nodeEnd <= reqEnd:
#         return nodes[index]
#     else:
#         left = query(index * 2, nodeStart, nodeMid, reqStart, reqEnd)
#         right = query(index * 2 + 1, nodeMid + 1, nodeEnd, reqStart, reqEnd)
#         return left + right         # min(left, right), max(left, rigtt) 등으로 변형 가능
#
#
# # 해당 index의 노드가 커버(포함)하는 구간 [nodeStart, nodeEnd]과 업데이트하는 노드의 인덱스와 값 reqIndex, newVal
# # 수정 : 1씩 증가
# def update(index, nodeStart, nodeEnd, reqIndex, newVal=1):
#     nodeMid = (nodeStart + nodeEnd) // 2
#     if nodeStart == nodeEnd:
#         nodes[index] += newVal
#     else:
#         if reqIndex <= nodeMid:
#             update(index * 2, nodeStart, nodeMid, reqIndex, newVal)
#         else:
#             update(index * 2 + 1, nodeMid + 1, nodeEnd, reqIndex, newVal)
#         nodes[index] = nodes[index * 2] + nodes[index * 2 + 1]  # min(left, right), max(left, rigtt) 등으로 변형 가능
#
#
# N = int(input())
# A = list(map(int, input().split()))
#
# # segment tree
# size = N
# count = [0] * N
# original = count
# nodes = [0] * (4 * size)
#
#
# for i in range(N):
#     # update A[i] (given by prev)
#     # Want to know : the number of elements of unsorted array 'give' which is greater than A[i]
#     A[i] += query(1, 0, N-1, i, N-1)
#
#     remain = N - (i + 1)
#     if A[i] >= remain:
#         update(1, 0, N-1, N-1)
#         A[i] -= remain
#     else:
#         update(1, 0, N-1, i + A[i])
#         A[i] = 0
#
#
# print(*A)


# Editorial : https://atcoder.jp/contests/abc388/editorial/12019
n = int(input())
a = list(map(int, input().split()))

c = [0] * n
d = [0] * (n + 1)  # 차분 배열 (나눠줄 돌의 개수를 관리), imos 알고리즘
# imos : https://velog.io/@nkrang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-imos-%EB%B2%95

for i in range(n):
    if i:
        c[i] = c[i - 1] + d[i]
        a[i] += c[i]

    cnt = min(n - i - 1, a[i])  # 나눠줄 수 있는 돌 개수 (남은 외계인 수와 현재 돌 개수 중 작은 값)
    a[i] -= cnt
    d[i + 1] += 1  # 돌을 나누는 시작점 설정
    d[min(n, i + cnt + 1)] -= 1  # 돌을 나누는 종료점 설정 : i+cnt+1번째 외계인 이후에는 돌을 받지 않음

print(*a)
