n = int(input('Digite um número de 1 a 50:'))

while n < 1 or n > 50:
    print('Número fora do intervalo, digite novamente:')
    n = int(input())
print('Número aceito')
