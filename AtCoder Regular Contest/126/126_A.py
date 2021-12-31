from itertools import permutations

T = int(input())
for _ in range(T):
    ans = 0
    N2, N3, N4 = map(int, input().split())
    for what_to_do in permutations('12345'):
        n2, n3, n4 = N2, N3, N4
        temp = 0
        for now in what_to_do:
            do = int(now)
            if do == 1:
                m = min(n3 // 2, n4)
                temp += m
                n3 -= m * 2
                n4 -= m
            if do == 2:
                m = min(n3 // 2, n2 // 2)
                temp += m
                n3 -= m * 2
                n2 -= m * 2
            if do == 3:
                m = min(n4 // 2, n2)
                temp += m
                n4 -= m * 2
                n2 -= m
            if do == 4:
                m = n2 // 5
                temp += m
                n2 -= m * 5
            if do == 5:
                m = min(n2 // 3, n4)
                temp += m
                n2 -= m * 3
                n4 -= m
        ans = max(ans, temp)
    print(ans)
