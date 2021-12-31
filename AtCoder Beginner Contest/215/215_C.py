# 참고: https://programmers.co.kr/learn/courses/4008/lessons/12836
from itertools import permutations
S, K = input().split()
S, K = list(S), int(K)-1
made = sorted(list(set(list(map(''.join, permutations(S))))))
print(made[K])
