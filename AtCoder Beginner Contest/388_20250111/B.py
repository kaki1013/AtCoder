N, D = map(int, input().split())
TL = [list(map(int, input().split())) for _ in range(N)]
for i in range(D):
    tmp = [t*(l+1+i) for t, l in TL]
    print(max(tmp))
