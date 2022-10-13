daysList = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

def checkLogin(login, days):

    if login in days:
        return True
    else:
        return False

def checkDays(days):

    if days > 6 or days < 0:
        return False
    else:
        return True

weekDay = False

while(not weekDay):
    dayLogin = input('Digite o dia da semana: ')
    weekDay = checkLogin(dayLogin, daysList)

waitTime = False

while(not waitTime):
    daysAmount = int(input('Quantidade de dias da entrega: '))
    waitTime = dayLogin(daysAmount)


if daysAmount == 0:
    print('Seu Pedido CHega Hoje!')
else:
    indexOfDay = daysList.index(dayLogin)
    newList = daysList[indexOfDay + 1:len(daysList)] + daysList[0:indexOfDay]

    delivery = newList[daysAmount - 1]

    print('Será entregue dia ', delivery)
