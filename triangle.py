x = input().split()
a, b, c = x
a = float(a)
b = float(b)
c = float(c)

Area = (((a + b) / 2) * 2)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Perimetro = {a + b + c:.1f}')
else:
    print(f'Area = {Area:.1f} ')
