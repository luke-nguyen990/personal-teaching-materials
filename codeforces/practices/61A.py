# https://codeforces.com/problemset/problem/61/A

a = input()
b = input()

ans = []

for i in range(len(a)):
    if a[i] != b[i]:
        ans += ['1']
    else:
        ans += ['0']

print(''.join(ans))
