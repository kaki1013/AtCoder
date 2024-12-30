N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

d = dict()
for i in range(N):
    a = A[i]
    if a in d:
        d[a].append(W[i])
    else:
        d[a] = [W[i]]

ans = 0
for k in d.keys():
    if len(d[k]) == 1:
        continue
    ans += sum(d[k])
    ans -= max(d[k])
print(ans)