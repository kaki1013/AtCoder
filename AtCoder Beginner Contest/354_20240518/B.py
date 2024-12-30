N = int(input())
arr = []
total = 0
for _ in range(N):
    S, C = input().split()
    arr.append(S)
    total += int(C)

arr.sort()
print(arr[total%N])
