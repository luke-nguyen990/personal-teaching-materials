# https://codeforces.com/problemset/problem/59/A


s = input()

is_lower = 0

for i, v in enumerate(s):
    if v.islower():
        is_lower += 1

if is_lower >= len(s) - is_lower:
    print(s.lower())
else:
    print(s.upper())
