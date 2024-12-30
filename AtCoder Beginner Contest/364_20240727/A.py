N = int(input())
arr = [1 if input() == 'sweet' else 0 for _ in range(N)]
flag = True
for i in range(N-2):
    if arr[i] == arr[i+1] == 1:
        flag = False
print('Yes' if flag else 'No')