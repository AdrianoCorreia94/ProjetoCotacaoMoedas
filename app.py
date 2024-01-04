import requests
import json


def ultimos_dias():
    dias = int(input('Digite o numero de dias?\
                                  \n   >> '))
    return dias


def escolha_moeda():
    moeda = int(input('Digite a moeda desejada\
                    \n1 USD-BRL: Dolar para Real\
                    \n2 EUR-BRL: Euro para Real\
                    \n3 BTC-BRL: Bitcoin para Real\
                    \n >> '
                      ))
    return moeda


# lista com tipos de moeda
moedas = ['USD-BRL',
          'EUR-BRL',
          'BTC-BRL']

frequencias = ['last',
               'daily']

while True:
    moeda = escolha_moeda()
    if moeda > 3 or moeda <= 0:
        continue
    else:
        arg_moeda = moedas[moeda-1]
        break

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
        break
    else:
        arg_frequencia = frequencias[frequencia-1]
        break
    break

url_base = ('https://economia.awesomeapi.com.br/json')
url = (f'{url_base}/{arg_frequencia}/{arg_moeda}/{arg_dias}')
