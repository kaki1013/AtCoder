from collections import deque
a, N = map(int, input().split())
MAX = N * 2
vst = [False] * MAX

q = deque([(1, 0)])
vst[1] = True

breaker = False
while q:
    now, count = q.popleft()
    if now * a < MAX and not vst[now*a]:
        q.append((now*a, count+1))
        vst[now*a] = True
        if now*a == N:
            print(count+1)
            breaker = True
            break
    if now >= 10 and now % 10:
        string = str(now)
        nxt = int(string[-1] + string[:-1])
        if nxt < MAX and not vst[nxt]:
            q.append((nxt, count+1))
            vst[nxt] = True
            if nxt == N:
                print(count + 1)
                breaker = True
                break
if not breaker:
    print(-1)