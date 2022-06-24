# https://codeforces.com/problemset/problem/977/A


n, k = map(int, input().split())

while k > n % 10:
    k -= n % 10 + 1
    n //= 10

print(n - k)
