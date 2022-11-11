def adicionar(shop_list, cod_produto):
    shop_list.insert(len(shop_list), cod_produto)


def remover(shop_list, cod_produto):

    if not cod_produto in shop_list:
        print(f'código {cod_produto} não encontrado')
        return

    shop_list.remove(cod_produto)


def exibir(shop_list):
    print(*shop_list, sep=' ')


shop_list = list(input())

for element in shop_list:
    if element == ' ':
        shop_list.remove(element)

user_input = []
while not 'encerrar' in user_input:

    user_input = input().split(' ')
    operacao = user_input[0]  # operacao do usuario
    try:
        cod_produto = user_input[1]  # codigo do produto
    except:
        pass

    if operacao == 'adicionar':
        adicionar(shop_list, cod_produto)
    elif operacao == 'remover':
        remover(shop_list, cod_produto)
    elif operacao == 'exibir':
        exibir(shop_list)
