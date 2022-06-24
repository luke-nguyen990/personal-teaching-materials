# https://codeforces.com/problemset/problem/546/A


k, n, w = map(int, input().split())

total_require = (1 + w) * w * k // 2

print(max(0, total_require - n))
