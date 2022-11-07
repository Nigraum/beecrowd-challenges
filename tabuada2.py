a = int(input())
b = int(input())

if a > b:
    print('Nenhuma tabuada no intervalo!')
else:
    for n in range(a, b + 1):
        for num in range(1, 11):
            print(f'{n} x {num} = {num * n}')
        print('-' * 10)
