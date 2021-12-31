def min_difference(x, arr):
    if x <= arr[0]:
        return abs(x-arr[0])
    if x >= arr[-1]:
        return abs(x-arr[-1])
    left, right = 0, len(arr) - 1
    # arr[left] < x < arr[right]
    while right - left > 1:
        m = (left + right) // 2
        if x == arr[m]:
            return 0
        if x < arr[m]:
            right = m
        else:
            left = m
    return min(abs(arr[left]-x), abs(arr[right]-x))


N, M = map(int, input().split())
A, B = list(map(int, input().split())), list(map(int, input().split()))
B.sort()

min_diff = 10**9
for a in A:
    min_diff = min(min_diff, min_difference(a, B))

print(min_diff)
