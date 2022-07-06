# https://codeforces.com/problemset/problem/1328/A


case = int(input())

for i in range(case):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - (a % b))
