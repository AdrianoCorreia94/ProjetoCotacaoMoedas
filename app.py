import requests
import json

# funcao para captar o tipo de moeda que usuario deseja


def escolha_moeda():
    moeda = int(input('Digite a moeda desejada\
                    \n1 USD-BRL: Dolar para Real\
                    \n2 EUR-BRL: Euro para Real\
                    \n3 BTC-BRL: Bitcoin para Real\
                    \n >> '
                      ))
    return moeda


# funcao para captar a quantidade de ultimos dias
def ultimos_dias():
    dias = int(input('Digite o numero de dias?\
                                  \n   >> '))
    return dias


url_base = ('https://economia.awesomeapi.com.br/json')

# lista com tipos de moeda
moedas = ['USD-BRL',
          'EUR-BRL',
          'BTC-BRL']

frequencias = ['last',
               'daily']

# chamada para escolha do tipo de moeda
'''
    > caso o usuario digitar opcao invalida retornamos ao loop perguntando 
      novamente o tipo da moeda.
    > se usuario digitar escolha dentro do permitido, entao adicionamos o tipo 
      da moeda ao arg para utilizar na url
'''
while True:
    moeda = escolha_moeda()  # chamada da funcao escolha moeda
    if moeda > 3 or moeda <= 0:  # caso seja digitado escolha fora do padrao
        continue  # retornamos ao loop para perguntar novamente o tipo da moeda
    else:  # escolha dentro do padrao
        arg_moeda = moedas[moeda-1]  # adiciona o tipo da moeda ao arg
        break  # encerra-se a escolha da moeda

# chamada para escolha da frequencia
'''
    > caso o usuario digitar opcao invalida: retornamos ao loop 
      perguntando novamente a frequencia.
    > se usuario digitar escolher uma frequencia de ultimos dias, 
      chamamos a funcao para capturar a quantidade de dias,
      passamos como arg para url e
      finalizamos o processo de escollha de frequencia
    > se usuario optar por cotacao atualizada:
      montamos a url da moeda atualizada e
      termina-se o processo de escolha de frequencia. 
'''

while True:
    frequencia = int(input('Digite a frequencia desejada\
                           \n  1 Cotação atualizada (a cada 30s)\
                           \n  2 Cotação dos últimos dias\
                           \n    >> '))
    if frequencia > 2 or frequencia < 1:  # se o usuario digitar um opcao invalida, retornar novamente ao menu
        continue  # retornando ao menu
    elif frequencia == 2:
        arg_dias = ultimos_dias()
        arg_frequencia = frequencias[frequencia-1]
        url = (f'{url_base}/{arg_frequencia}/{arg_moeda}/{arg_dias}')
        break
    else:
        arg_frequencia = frequencias[frequencia-1]
        url = (f'{url_base}/{arg_frequencia}/{arg_moeda}')
        break
    break
