qtd_canais = int(input())

user_input = []
channels = []
for i in range(qtd_canais):

    user_input = input().split(';')

    channel = {}
    # get parameters
    channel['name'] = user_input[0]
    channel['subscribers'] = int(user_input[1])
    channel['monetization'] = float(user_input[2])
    channel['premium'] = True if user_input[3] == 'sim' else False

    channels.append(channel)

taxa_x = float(input())
taxa_y = float(input())

print('-----')
print('BÔNUS')
print('-----')

for channel in channels:
    tax = taxa_x if channel['premium'] == True else taxa_y
    bonus = channel['monetization'] + tax * \
        int((channel['subscribers'] / 1000))
    print(f'{channel["name"]}: R$ {bonus:.2f}')
