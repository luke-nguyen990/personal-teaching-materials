# https://codeforces.com/problemset/problem/155/A

length = int(input())

A = list(map(int, input().split()))
cur_min, cur_max = A[0], A[0]
ans = 0
for i in range(1, length):
    if A[i] > cur_max or A[i] < cur_min:
        ans += 1
        cur_min = min(cur_min, A[i])
        cur_max = max(cur_max, A[i])
print(ans)
