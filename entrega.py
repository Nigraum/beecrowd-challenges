dayList = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
buy = input()
deliveryD = int(input())
buyDate = dayList.index(buy)
delivery = dayList[(buyDate + deliveryD) % len(dayList)]

if deliveryD == 0:
    print('chega hoje!')
else:
    print(f'sera entregue {delivery}')

