z = input().split()
x, y = z

if float(x) < 0 and float(y) > 0:
    print('Q2')

if float(x) < 0 and float(y) < 0:
    print('Q3')

if float(x) > 0 and float(y) < 0:
    print('Q4')

if float(x) > 0 and float(y) > 0:
    print('Q1')

if float(x) == 0:
    if float(y) == 0:
        print('Origem')
    if float(y) != 0:
        print('Eixo Y')
if float(y) == 0:
    if float(x) != 0:
        print('Eixo X')
