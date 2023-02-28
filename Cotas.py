import re
import requests
global DolarCota
global BTCCota


def dolar_reais():
    global DolarCota
    # Faz a requisição HTTP para a página que contém o valor atual do salário mínimo
    url = 'https://www.google.com/search?client=opera-gx&q=cotação+dolar+real&sourceid=opera&ie=UTF-8&oe=UTF-8'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem sucedida
    except requests.exceptions.RequestException as e:
        print(f'Erro ao fazer requisição HTTP: {e}')
        exit()

    # Extrai o valor da cotação Dolar/Real da resposta HTTP usando uma expressão regular
    DolarCota_str = re.search(r"(\d+\,\d{2})\s+Real", response.text)
    if DolarCota_str:
        DolarCota_str = DolarCota_str.group(1).replace('.', '').replace(
            ',', '.').replace('Real', '')  # Converte para um formato de ponto flutuante
        DolarCota = float(DolarCota_str)
        if __name__ == "__main__":
            print('1 dolar hoje vale R${}'.format(DolarCota))
    else:
        print('Não foi possível obter o valor da cotação atual')


def BTC_Real():
    global BTCCota
    # Faz a requisição HTTP para a página que contém o valor atual do salário mínimo
    url = 'https://www.google.com/search?q=cotação+bitcoin+real&client=opera-gx&sxsrf=AJOqlzUYSoRele3QB_IdjUnpiGIva8g8aA%3A1677540178033&ei=Ujv9Y_7VAceb1sQPjbGc8AU&ved=0ahUKEwj-xqGT7Lb9AhXHjZUCHY0YB14Q4dUDCA4&oq=cotação+bitcoin+real&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQDEoECEEYAFAAWABgAGgAcAF4AIABAIgBAJIBAJgBAA&sclient=gws-wiz-serp'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem sucedida
    except requests.exceptions.RequestException as e:
        print(f'Erro ao fazer requisição HTTP: {e}')
        exit()

    # Extrai o valor da cotação Dolar/Real da resposta HTTP usando uma expressão regular
    BTCCota_str = re.search(r"(\d+\.\d+,\d{2})", response.text)
    if BTCCota_str:
        BTCCota_str = BTCCota_str.group(1).replace('.', '').replace(
            ',', '.')  # Converte para um formato de ponto flutuante
        BTCCota = float(BTCCota_str)
        if __name__ == "__main__":
            print('1 BTC hoje vale R${}'.format(BTCCota))
    else:
        print('Não foi possível obter o valor da cotação atual')


if __name__ == "__main__":
    def Executar():
        dolar_reais()
        BTC_Real()


if __name__ == "__main__":
    Executar()
