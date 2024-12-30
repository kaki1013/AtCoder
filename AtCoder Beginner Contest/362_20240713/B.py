x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

def get_dist2(x1, y1, x2, y2):
    return (x1-x2)**2+(y1-y2)**2

dist2 = [get_dist2(x1, y1, x2, y2), get_dist2(x2, y2, x3, y3), get_dist2(x3, y3, x1, y1)]
dist2.sort()

a, b, c = dist2
flag = (a+b==c)
print('Yes' if flag else 'No')
