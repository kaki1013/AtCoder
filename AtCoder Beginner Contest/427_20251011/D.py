# 게임 이론 문제 경험 부족 이슈.. (bob 차례에는 ) : 늦은 AC...
def get_winner(adj, dp, num_of_left_turn, turn, position):
    if turn == 1:  # bob
        check = dp[num_of_left_turn-1][0]
    else:  # alice
        check = dp[num_of_left_turn][1]

    want = 'Alice' if turn == 0 else 'Bob'
    for v in adj[position]:
        if check[v] == want:
            return want
    return 'Alice' if turn == 1 else 'Bob'


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    S = input()
    adj = [[] for _ in range(N+1)]
    adj_inv = [[] for _ in range(N+1)]
    for __ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj_inv[v].append(u)

    # dp[num_of_left_turn][turn][position] = winner
    # dp[0~K][0~1(0:alice, 1:bob)][1~N]= Alice or Bob
    dp = [[[-1] * (N+1) for _ in range(2)] for _ in range(K+1)]

    # last state
    for pos in range(N):
        dp[0][0][pos+1] = 'Alice' if S[pos] == 'A' else 'Bob'
        dp[0][1][pos+1] = 'Alice' if S[pos] == 'A' else 'Bob'

    # fill dp
    for turn in range(1, K+1):
        for pos in range(1, N+1):
            # check bob first
            dp[turn][1][pos] = get_winner(adj, dp, turn, 1, pos)

        for pos in range(1, N+1):
            # check alice last
            dp[turn][0][pos] = get_winner(adj, dp, turn, 0, pos)

    print(dp[K][0][1])
