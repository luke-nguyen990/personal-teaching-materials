# https://codeforces.com/problemset/problem/282/A


C = int(input())

answer = 0
while C:
    if input()[1] == '+':
        answer += 1
    else:
        answer -= 1
    C -= 1
print(answer)
