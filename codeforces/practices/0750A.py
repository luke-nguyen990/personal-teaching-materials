# https://codeforces.com/problemset/problem/750/A

from math import ceil

num_problems, total_minutes = map(int, input().split())
avai_minutes = 240 - total_minutes

c = - (avai_minutes // 5) * 2
a, b = 1, 1

delta = b*b - 4*a*c
ans = (-b + (delta**(1/2)))/2

print(min(int(ans), num_problems))
