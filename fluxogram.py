n = int(input())
qtd = 0
d = 1

while d <= n:
    if n % d == 0:
        qtd += 1
    d += 1
if qtd == 2:
    print('Primo')
else:
    print('Nao primo')
