c = int(input())

for cc in range(c):
    r1 = input()
    r2 = input()
    if r1.count('1') + r2.count('1') == 4:
        print(2)
    elif '1' in r1 or '1' in r2:
        print(1)
    else:
        print(0)
