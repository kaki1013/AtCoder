"""
operations: R, M
R:1, M:1, RMR:M^-1, MRM=R
앞->뒤: 1, 뒤->앞: min(3, n-1), 거꾸로: 1
"""
n = int(input())
p = list(map(int, input().split()))
r, m, reverse_m = 1, 1, min(3, n-1)
is_reversed = False
case = []
start = p.index(1)
if p[(start + 1) % n] != 2:
    is_reversed = True
    case.append(m * (start + 1) + int(is_reversed))
    case.append(reverse_m * (n - start - 1) + int(is_reversed))
    case.append(r + m * (n - start - 1) + r + int(is_reversed))   # m^-k = rm^kr
    p = p[::-1]
start = p.index(1)
case.append(m * start + int(is_reversed))
case.append(reverse_m * (n - start) + int(is_reversed))
case.append(r + m * (n - start) + r + int(is_reversed))
print(min(case))
