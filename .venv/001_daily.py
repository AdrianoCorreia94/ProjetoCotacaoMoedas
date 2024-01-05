"""
    > Meu primeiro projeto para consultar valor de moedas convertido em reais.
    > O projeto é tem como fim trabalhar com api request e ir aumento o nível de 
      complexidade futuramente, logo, este é meu marco zero. 
    > Objetivo da aplicacao: 
        consultar valores atualizados de uma moeda convertida em reais.
"""

import requests
import json


# funcao para capturar o tipo de moeda que usuario deseja
def escolha_moeda():
    moeda = int(input('Digite a moeda desejada\
                    \n1 USD-BRL: Dolar para Real\
                    \n2 EUR-BRL: Euro para Real\
                    \n3 BTC-BRL: Bitcoin para Real\
                    \n >> '
                      ))
    return moeda


# funcao para mostrar resultado da daily
def resultado_daily():
    url = (f"{url_base}/{arg_moeda}")
    arg_compra = arg_moeda.replace('-', '')
    result = requests.get(url)
    compra = json.loads(result.text)[arg_compra]
    print('\nRESULTADO: \n')
    for x, y in compra.items():
        print(f'{x}: {y}')


url_base = ('https://economia.awesomeapi.com.br/json/last/')


# lista com tipos de moeda
moedas = ['USD-BRL',
          'EUR-BRL',
          'BTC-BRL']

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
        resultado_daily()
        break  # encerra-se a escolha da moeda
