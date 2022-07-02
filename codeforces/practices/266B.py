# https://codeforces.com/problemset/problem/266/B


l, m = map(int, input().split())

S = list(input())

for i in range(m):
    j = 0
    while j < l - 1:
        if S[j] == 'B' and S[j + 1] == 'G':
            S[j], S[j + 1] = S[j + 1], S[j]
            j += 1
        j += 1

print(''.join(S))
