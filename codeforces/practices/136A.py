# https://codeforces.com/problemset/problem/136/A


length = int(input())

A = list(map(int, input().split()))

ans = [None for i in range(length)]

for i, v in enumerate(A):
    ans[v - 1] = i + 1

for a in ans:
    print(a, end=' ')
