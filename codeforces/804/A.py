n = int(input())

while n:
    cur = int(input())
    if cur % 2 == 1:
        print(-1)
    elif cur % 2 == 0:
        print(0, 0, cur // 2)
    n -= 1
