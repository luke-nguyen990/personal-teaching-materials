# https://codeforces.com/problemset/problem/520/A


length = int(input())
s = input().lower()

if len(set(s)) == 26:
    print("YES")
else:
    print("NO")
