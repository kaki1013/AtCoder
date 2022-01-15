N = int(input())
H = list(map(int, input().split()))
ans = H[0]
for i in range(1, N):
    if ans < H[i]:
        ans = H[i]
        continue
    break
print(ans)