# https://codeforces.com/problemset/problem/467/A


number_of_cases = int(input())
answer = 0
while number_of_cases:
    p, q = map(int, input().split())
    if p + 2 <= q:
        answer += 1
    number_of_cases -= 1

print(answer)
