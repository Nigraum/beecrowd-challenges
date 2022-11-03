first_case = int(input())

for case in range(first_case):
    n = int(input())

    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    if isPrime:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')

