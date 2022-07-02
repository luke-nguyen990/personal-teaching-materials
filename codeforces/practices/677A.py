# https://codeforces.com/problemset/problem/677/A


n, h = map(int, input().split())

A = list(map(int, input().split()))

total_width = 0

for i, v in enumerate(A):
    total_width += 1
    if v > h:
        total_width += 1

print(total_width)
