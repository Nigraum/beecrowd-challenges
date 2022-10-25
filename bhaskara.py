values = input().split()
a, b, c = values
a = float(a)
b = float(b)
c = float(c)

if a == 0 or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x2 = (- b - (b **2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    print('R1 = %.5f' %x1)
    print('R2 = %.5f' %x2)
