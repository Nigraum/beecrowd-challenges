price = float(input())
unit = int(input())
totalPrice = unit * price
totalPriceDiscout = totalPrice - (totalPrice * ((10 + unit) / 100))
print('%.2f' %totalPrice)
print('%.2f' %totalPriceDiscout)



