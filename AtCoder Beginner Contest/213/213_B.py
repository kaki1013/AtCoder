N = int(input())
A = list(map(int, input().split()))

scores = []
for i in range(N):
    scores.append((A[i], i + 1))

scores.sort(reverse=True)

print(scores[1][1])
