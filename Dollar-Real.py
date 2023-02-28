import Cotas

Cotas.dolar_reais()

while True:
    valor = input('Quantos reais você quer gastar para comprar dolar?')
    try:
        valor = float(valor)
        print('Com R${} da para comprar ${}'.format(
            valor, valor/Cotas.DolarCota))
        break
    except ValueError:
        print('O Valor inserido não é permitido. Somente números e ponto')
    except TypeError:
        print('O Valor inserido não é permitido. Somente números e ponto')
