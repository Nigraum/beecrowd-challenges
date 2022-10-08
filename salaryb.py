name = input()
salary = float(input())
totalSales = float(input())
comission = float(totalSales * (15 / 100))
total = salary + comission
print('TOTAL = R$ %.2f' %total)
