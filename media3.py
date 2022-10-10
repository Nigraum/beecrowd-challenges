a = float(input())
b = float(input())
media = (a + b) / 2
if a == 0:
    print('reprovado')
elif media >= 6:
    print('aprovado')
elif media <= 0.995:
    print('reprovado')
else:
    print('talvez com a sub')

