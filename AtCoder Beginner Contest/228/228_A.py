S, T, X = map(int, input().split())

ans = 'No'
if S <= X < T:
    ans = 'Yes'
elif S > T:
    if X >= S or X < T:
        ans = 'Yes'

print(ans)
