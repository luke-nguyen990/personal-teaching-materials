

from cmath import inf


C = int(input())

while C:
    n = int(input())
    Stones = list(map(int, input().split()))
    cur = 0
    if len(Stones) % 2:
        print('Mike')
    else:
        minM = inf
        indM = inf
        minJ = inf
        indJ = inf
        for i, v in enumerate(Stones):
            if i % 2 == 0:
                if v < minM:
                    minM = v
                    indM = i
            else:
                if v < minJ:
                    minJ = v
                    indJ = i
        if minM == minJ:
            if indM < indJ:
                print('Joe')
            else:
                print('Mike')
        elif minM < minJ:
            print('Joe')
        else:
            print('Mike')

    C -= 1
