# https://codeforces.com/problemset/problem/734/A


length = int(input())
s = input()

a = s.count('A')
d = length - a

if a == d:
    print('Friendship')
elif a > d:
    print('Anton')
else:
    print('Danik')
