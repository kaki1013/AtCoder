# BOJ 18870 좌표압축 참고함
H, W, N = map(int, input().split())
locate = [tuple(map(int, input().split())) for _ in range(N)]

sorted_locate_x = sorted(locate)
sorted_locate_y = sorted(locate, key=lambda x: x[1])

locate_dict_x = dict()
locate_dict_y = dict()

key_x = 1
for n, _ in sorted_locate_x:
    if n not in locate_dict_x:
        locate_dict_x[n] = key_x
        key_x += 1

key_y = 1
for _, n in sorted_locate_y:
    if n not in locate_dict_y:
        locate_dict_y[n] = key_y
        key_y += 1

for x, y in locate:
    print(locate_dict_x[x], locate_dict_y[y])