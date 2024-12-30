N = int(input())
arr = []
for i in range(N):
    A, C = map(int, input().split())
    arr.append((A, C, i+1))
arr.sort(reverse=True)

remain = [arr[0][2]]
prev_cost = arr[0][1]
for i in range(1, N):
    A, C, idx = arr[i]
    if C > prev_cost:
        continue
    remain.append(idx)
    prev_cost = C

print(len(remain))
print(*sorted(remain))
