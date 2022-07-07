# https://codeforces.com/problemset/problem/141/A


A = input()
B = input()
_AB = sorted(A + B)
AB = sorted(input())

if _AB == AB:
    print("YES")
else:
    print("NO")
