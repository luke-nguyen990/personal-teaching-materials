# https://codeforces.com/problemset/problem/1335/A


case = int(input())

for c in range(case):
    n = int(input())
    print(max(0, (n + 1) // 2 - 1))
