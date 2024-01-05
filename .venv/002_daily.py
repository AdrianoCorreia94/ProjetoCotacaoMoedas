"""
    > Segundo Projeto de Cotacao de moedas:
    > Objetivo: 
        * adicionar mais de uma moeda na cotacao 
        * retornar resultado como um dataframe
"""

import requests
import json
import pandas as pd

# funcao para capturar o tipo de moeda que usuario deseja


def escolha_moeda():
    moeda = int(input('Digite a moeda desejada\
                    \n1 USD-BRL: Dolar para Real\
                    \n2 EUR-BRL: Euro para Real\
                    \n3 BTC-BRL: Bitcoin para Real\
                    \n >> '
                      ))
    return moeda


"""
    > funcao para retornar os valores solicitados pelo usuario
    > o resultado final sera visualizado em formato dataframe
"""


def resultado_busca():
    url = (f"{url_base}{escolhas}")  # montar url com moedas escolhidas
    r = requests.get(url).text  # fazer o request da moeda
    r = json.loads(r)  # carregar em formato json
    teste = pd.DataFrame(r)  # ler o json com pandas e transformar em dataframe
    return print(teste)  # retornar o resultado


# url basica da busca de cotacao atual
url_base = ('https://economia.awesomeapi.com.br/json/last/')

# lista de moedas a serem escolhidas
moedas = ['USD-BRL', 'EUR-BRL', 'BTC-BRL']

# variavel para completar a url na hora de solicitar requests
escolhas = ""

while True:
    tipo_moeda = escolha_moeda()
    if tipo_moeda > 3 or tipo_moeda < 1:
        continue
    else:
        escolhas = escolhas + (moedas[tipo_moeda-1])
        continuar = int(input('Deseja incluir outra moeda?\
              \n1 Sim\
              \n2 Nao'))
        if continuar == 1:
            # inclusao da virgula no final de cada moeda escolhida,
            # a utlima moeda deve ficar sem virgula no final para nao haver erro na url
            escolhas = escolhas + ','
            continue
        else:
            resultado_busca()
            break
