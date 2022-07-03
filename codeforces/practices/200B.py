# https://codeforces.com/problemset/problem/200/B


n = int(input())

drinks = list(map(int, input().split()))

print(sum(drinks) / n)
