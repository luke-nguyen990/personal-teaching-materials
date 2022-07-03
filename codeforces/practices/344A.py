# https://codeforces.com/problemset/problem/344/A


number_of_magnets = int(input())

total_groups = 0

prev_magnet = None

while number_of_magnets:
    cur_magnet = input()
    if cur_magnet != prev_magnet:
        prev_magnet = cur_magnet
        total_groups += 1
    number_of_magnets -= 1
print(total_groups)
