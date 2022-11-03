debt = int(input())
payMonthly = int(input())
payment = 0

while debt > 0:
    payment += 1
    print(f'pagamento: {payment}')
    print(f'antes = {debt}')

    if payMonthly < debt:
        debt -= payMonthly
    else:
        debt = 0
    print(f'depois = {debt}')
    print('-' * 5)
