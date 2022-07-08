# https://codeforces.com/problemset/problem/510/A


R, C = map(int, input().split())

for r in range(R):
    if r % 2:
        if r % 3 == 1:
            print('.' * (C - 1) + '#')
        else:
            print('#' + '.' * (C - 1))
    else:
        print('#'*C)
