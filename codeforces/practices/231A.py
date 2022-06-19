C = int(input())

total = 0
while C:
    x = list(map(int, input().split()))

    if x.count(1) > 1:
        total += 1

    C -= 1
print(total)
