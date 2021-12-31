# 두 그룹 a와 b로 나누고 나서는 a,b 내에서는 내림차순으로 나열
N = input()
l = len(N)

ans = 0
for i in range(1, 1 << l - 1):  # 한 쪽에 몰리는 것 방지
    a, b = [], []
    for j in range(l):
        if i & (1 << j):
            a.append(N[j])
        else:
            b.append(N[j])
    if set(a) == {'0'} or set(b) == {'0'}:
        continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    a = int(''.join(a))
    b = int(''.join(b))
    ans = max(ans, a * b)
print(ans)
