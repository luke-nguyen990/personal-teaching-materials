# https://codeforces.com/problemset/problem/144/A


length = int(input())
A = list(map(int, input().split()))
max_index = A.index(max(A))
min_index = length - 1 - A[::-1].index(min(A))

ans = max_index - 0 + length - 1 - min_index

if max_index > min_index:
    ans -= 1

print(ans)
