C = int(input())

while C:
    n, m = map(int, input().split())
    board = [[0 for c in range(m)] for r in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                if j % 4 == 0 or j % 4 == 3:
                    board[i][j] = '1'
                else:
                    board[i][j] = '0'
            elif i % 2 == 1:
                if board[i-1][j] == '1':
                    board[i][j] = '0'
                else:
                    board[i][j] = '1'
            elif i % 2 == 0:
                if board[i-1][j] == '0':
                    board[i][j] = '0'
                else:
                    board[i][j] = '1'
        print(' '.join(board[i]))
    C -= 1
