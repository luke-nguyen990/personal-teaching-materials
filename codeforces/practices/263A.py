# https://codeforces.com/problemset/problem/263/A


row, col = 5, 5

ans = None

for i in range(row):
    cur_row = input().split()
    if '1' in cur_row:
        ans = abs(2 - i) + abs(2 - cur_row.index('1'))

print(ans)
