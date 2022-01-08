K = int(input())
ans = []
for i in bin(K)[2:]:
    if int(i):
        ans.append('2')
    else:
        ans.append('0')
print(''.join(ans))