# https://codeforces.com/problemset/problem/443/A


char_set = set()

for a in input():
    if a.isalpha():
        char_set.add(a)

print(len(char_set))
