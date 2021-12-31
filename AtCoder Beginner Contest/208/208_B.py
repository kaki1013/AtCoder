P = int(input())
factorial = [1, 1]
for i in range(2, 11):
    factorial.append(factorial[i-1]*i)

i = 10
count = 0
while True:
    if P == 0:
        break
    if P >= factorial[i]:
        count += P // factorial[i]
        P %= factorial[i]
    i -= 1
print(count)