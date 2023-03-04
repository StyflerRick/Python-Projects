while True:
    try:
        numero = int(input('Digite um numero:'))
    except ValueError:
        print('Value Error: Digite apenas numeros inteiros.')
    except TypeError:
        print('Type Error: Digite apenas numeros inteiros.')
