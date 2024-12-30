cost = list(map(int, input().split()))
c = {'Red':0, 'Green':1, 'Blue':2}[input()]

cost = cost[:c]+cost[c+1:]
print(min(cost))