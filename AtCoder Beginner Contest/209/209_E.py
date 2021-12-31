from sys import stdin
input = stdin.readline
N = int(input().strip())
words = []
words_end = dict()
words_start = dict()
for _ in range(N):
    word = input().strip()
    words.append(word)

    end_key = word[-3:]
    if end_key in words_end:
        words_end[end_key].append(word)
    else:
        words_end[end_key] = [word]

    start_key = word[:3]
    if start_key in words_start:
        words_start[start_key].append(word)
    else:
        words_start[start_key] = [word]

used_start = set()
count = 0  # 홀 T 짝 A
for word in words:
    while True:
        pass