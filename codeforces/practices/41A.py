# https://codeforces.com/problemset/problem/41/A


S = input()
R = input()

if ''.join(R[::-1]) == S:
    print('YES')
else:
    print('NO')
