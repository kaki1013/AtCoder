N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

dp1 = [0]
dp2 = [0]
for i in range(N):
    dp1.append(dp1[-1]+A[i])
    dp2.append(dp2[-1]+B[i])

flag = True
for i in range(N+1):
    if dp1[i] > X or dp2[i] > Y:
        print(i)
        flag = False
        break
if flag:
    print(N)