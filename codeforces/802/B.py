C = int(input())


while C:
    length = int(input())
    original_number = input()
    sum_number = 0
    if original_number[0] != '9':
        sum_number = int('9' * length)
    else:
        sum_number = (10 ** length + 1) + 10 + 10**(length - 1)
    print(sum_number - int(original_number))
    C -= 1
