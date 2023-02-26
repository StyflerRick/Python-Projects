from string import ascii_letters
validos = ascii_letters + ' '


def names():
    while True:
        name = input('Digite seu Nome:')
        if all(c in validos for c in name):
            print('Muito Prazer, {}'.format(name))
            break
        else:
            print('Apenas caracteres são permitidos')


names()


def ages():
    global myage
    while True:
        myage = (input('Digite sua Idade:'))
        if myage.isdigit():
            print('A informação foi guardada')
            break
        else:
            print('Apenas Numeros são permitidos')


ages()
