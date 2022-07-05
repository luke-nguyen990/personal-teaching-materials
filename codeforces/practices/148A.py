# https://codeforces.com/problemset/problem/148/A


k, ll, m, n = int(input()), int(input()), int(input()), int(input())
d = int(input())
ans = 0
for i in range(1, d + 1):
    if i % k == 0 or i % ll == 0 or i % m == 0 or i % n == 0:
        ans += 1
print(ans)
