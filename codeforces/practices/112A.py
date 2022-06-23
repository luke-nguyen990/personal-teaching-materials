# https://codeforces.com/problemset/problem/112/A


A = input().lower()
B = input().lower()

if A > B:
    print(1)
elif A < B:
    print(-1)
else:
    print(0)
