a = input().split()
b = input().split()

c1, n1, v1 = a
c2, n2, v2 = b

total = ((int(n1) * float(v1)) + (int(n2) * float(v2)))

print('VALOR A PAGAR: R$ %.2f' %total)
