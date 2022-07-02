# https://codeforces.com/problemset/problem/734/A


l = int(input())

s = input()

a = s.count('A')
d = l - a

if a == d:
    print('Friendship')
elif a > d:
    print('Anton')
else:
    print('Danik')
