vC = float(input())
totalVC = 0

while vC != -1.0:
    totalVC += vC
    vC = float(input())

total = totalVC * 2.50
print('VC$ %.2f' %totalVC)
print('R$ %.2f' %total)

