# https://codeforces.com/problemset/problem/996/A

total = int(input())
ans = 0
bills = [100, 20, 10, 5, 1]
for b in bills:
    ans += total // b
    total %= b
print(ans)
