# https://codeforces.com/problemset/problem/266/A


n = int(input())

s = input()

latest = None

ans = 0

for i, v in enumerate(s):
    if latest != v:
        latest = v
    else:
        ans += 1

print(ans)
