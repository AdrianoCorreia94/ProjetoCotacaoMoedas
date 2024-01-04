import requests
import json

# lista com tipos de moeda
moedas = ['USD-BRL',
          'EUR-BRL',
          'BTC-BRL']


while True:
    moeda = int(input('Digite a moeda desejada\
                    \n1 USD-BRL: Dolar para Real\
                    \n2 EUR-BRL: Euro para Real\
                    \n3 BTC-BRL: Bitcoin para Real\
                    \n >> '
                      ))
    if moeda > 3 or moeda <= 0:
        continue
    else:
        arg_moeda = moedas[moeda-1]
        break

print(arg_moeda)
