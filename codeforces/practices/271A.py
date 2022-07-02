# https://codeforces.com/problemset/problem/271/A


cur_year = int(input())

while True:
    cur_year += 1
    if len(str(cur_year)) == len(set(str(cur_year))):
        print(cur_year)
        break
