# https://codeforces.com/problemset/problem/791/A


from math import log

a, b = map(int, input().split())


ans = int(log(b/a, 1.5)) + 1

print(ans)
