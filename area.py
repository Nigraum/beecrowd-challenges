value = input().split()
a, b, c = value
triangleArea = (float(a) * float(c)) / 2
circleArea = 3.14159 * float(c) ** 2
trapezeArea = ((float(a) + float(b)) * float(c)) / 2
squareArea = float(b) ** 2
rectangleArea = float(a) * float(b)
print('TRIANGULO: %.3f' %triangleArea)
print('CIRCULO: %.3f' %circleArea)
print('TRAPEZIO: %.3f' %trapezeArea)
print('QUADRADO: %.3f' %squareArea)
print('RETANGULO: %.3f' %rectangleArea)
