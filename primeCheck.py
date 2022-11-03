a = int(input())

for i in range(0, a):
    number = int(input())
    b = 0
    c = 1
    while c <= number:
        if number % c == 0:
            b = b + 1
        c = c + 1
    if b > 2:
        print(f'{number} nao eh primo')
    else:
        print(f'{number} eh primo')
