listaDeDias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

def verificaDiaEntrada(entrada, lista):
    
    if entrada in lista:
        return True
    else:
        return False

def verificaQuantDeDias(dias):
    
    if dias > 6 or dias < 0:
        return False
    else:
        return True 

diaDaSemana = False

while(not diaDaSemana):
    diaEntrada = input('Digite o dia da semana: ')
    diaDaSemana = verificaDiaEntrada(diaEntrada, listaDeDias)
    
prazoDeEspera = False

while(not prazoDeEspera):
    quantDias = int(input('Quantidade de dias da entrega: '))
    prazoDeEspera = verificaQuantDeDias(quantDias)
    

if quantDias == 0:
    print('Seu Pedido CHega Hoje!')
else:
    indexDoDiaSemana = listaDeDias.index(diaEntrada)
    novaLista = listaDeDias[indexDoDiaSemana + 1:len(listaDeDias)] + listaDeDias[0:indexDoDiaSemana]

    diaEntrega = novaLista[quantDias - 1]

    print('Será entregue dia ', diaEntrega)