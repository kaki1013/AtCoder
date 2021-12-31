A, B = map(int, input().split())

if A == 0 or B == 0:
    if B == 0:
        print('Gold')
    if A == 0:
        print('Silver')
else:
    print('Alloy')
