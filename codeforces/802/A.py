C = int(input())


while C:
    n, m = map(int, input().split())
    if m != 1:
        total = (1 + m) * m // 2
        if m != 1:
            first_term = m * 2
            last_term = m * n
            num = n - 1
            total += (first_term + last_term) * num // 2
        print(total)
    else:
        print((1 + n) * n // 2)
    C -= 1
