# https://codeforces.com/problemset/problem/71/A


C = int(input())

while C:
    w = input()
    if len(w) > 10:
        print(f'{w[0]}{len(w)-2}{w[-1]}')
    else:
        print(w)
    C -= 1
