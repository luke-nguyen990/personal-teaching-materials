# https://codeforces.com/problemset/problem/268/A


from collections import defaultdict

case = int(input())
home = defaultdict(int)
away = defaultdict(int)
ans = 0
for i in range(case):
    h, a = map(int, input().split())
    ans += home[a] + away[h]
    home[h] += 1
    away[a] += 1

print(ans)
