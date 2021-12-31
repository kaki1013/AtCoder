N = int(input())
stack = []
if N == 1:
    stack.append('A')
else:
    while N != 1:
        if N == 0:
            N += 1
            stack.append('A')
        elif N % 2 == 0:
            N //= 2
            stack.append('B')
        else:
            N -= 1
            stack.append('A')
    stack.append('A')

print(''.join(stack[::-1]))
