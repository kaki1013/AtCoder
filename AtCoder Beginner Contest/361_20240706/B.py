# a, b, c, d, e, f = list(map(int, input().split()))
# g, h, i, j, k, l = list(map(int, input().split()))
#
# points = [(a, b, c), (a, b, f), (a, e, c), (a, e, f), (d, b, c), (d, b, f), (d, e, c), (d, e, f)]
# flag = False
# for p, q, r in points:
#     if (g < p < j) or (h < q < k) or (i < r < l):
#         flag = True
#         break
#
# points = [(g, h, i), (g, h, l), (g, k, i), (g, k, l), (j, h, i), (j, h, l), (j, k, i), (j, k, l)]
# for p, q, r in points:
#     if (a < p < d) or (b < q < e) or (c < r < f):
#         flag = True
#         break
# print('Yes' if flag else 'No')
a,b,c,d,e,f = list(map(int, input().split()))
g,h,i,j,k,l = list(map(int, input().split()))

points = [(a, b, c), (a, b, f), (a, e, c), (a, e, f), (d, b, c), (d, b, f), (d, e, c), (d, e, f)]
flag = False
for p, q, r in points:
    if (g < p < j) and (h < q < k) and (i < r < l):
        flag = True
        break
print('Yes' if flag else 'No')
