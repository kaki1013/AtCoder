"""
2^N : real key가 True, 아니면 False인 경우들
M개의 test
C_i개의 예비 키값들 비교하면서 맞는지 체크
O(MN2^N) -> 15*100*2^15 = 5*10^7 (49152000)

M개의 test
    각 경우들이 test 통과(각 A[i]와 cand 비교하여 일치하는 개수가 K개 이상)하면 그대로 유지

"""

N, M, K = map(int, input().split())
candidate = [i for i in range(1 << N)]  # possible keys

for _ in range(M):
    tmp = input().split()
    C, A, R = tmp[0], tmp[1:-1], tmp[-1]
    C = int(C)
    A = list(map(lambda x: int(x) - 1, A))  # zero base
    R = True if R == "o" else False

    tmp = []
    for cand in candidate:
        count = 0  # >= K ?
        for i in A:
            if cand & (1 << i):
                count += 1

        if (R and count >= K) or (not R and count < K):
            # 여전히 가능한 것들 tmp에 넣기
            tmp.append(cand)

    candidate = tmp

print(len(candidate))
