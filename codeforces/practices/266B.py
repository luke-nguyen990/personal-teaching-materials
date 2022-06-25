# https://codeforces.com/problemset/problem/266/B


l, m = map(int, input().split())

S = list(input())
last_available = None

for i in range(l - 1, -1, -1):
    if S[i] == 'G' and last_available == None:
        last_available = i
    elif S[i] == 'B':
        if last_available:
            new_pos = min(last_available, i + m)
            S[i], S[new_pos] = S[new_pos], S[i]
            last_available = new_pos - 1
print(''.join(S))
