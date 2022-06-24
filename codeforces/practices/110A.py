# https://codeforces.com/problemset/problem/110/A


X = input()

total_lucky_digits = X.count('4') + X.count('7')

if total_lucky_digits == 7 or total_lucky_digits == 4:
    print('YES')
else:
    print('NO')
