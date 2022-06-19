from cmath import inf

C = int(input())
while C:
    r, c = map(int, input().split())
    board = []
    maxNum = -inf
    for i in range(r):
        row = list(map(int, input().split()))
        board.append(row)
        maxNum = max(maxNum, max(row))
    curArea = inf
    for i in range(r):
        for j in range(c):
            if board[i][j] == maxNum:
                l = max(i + 1, r - i)
                h = max(j + 1, c - j)
                curArea = min(curArea, l * h)
    print(curArea)
    C -= 1
