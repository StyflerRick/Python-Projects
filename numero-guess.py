import random

tentativas = [1]
randomnum = random.randint(0, 100)  # Numero aleatorio de 0 a 100
randomnum = int(randomnum)  # Define variavel como 'int'
print('Numero aleatorio é {}'.format(randomnum))

while True:
    try:
        tentativa = int(input('Chute um numero de 0 a 100: '))
        if tentativa == randomnum:
            print('Você acertou o numero.')
            print(f'O numero aleatorio era {randomnum}.')
            break
        elif tentativa > 100:
            print('Somente numeros entre 0 e 100.')
            tentativas.append(1)
        else:
            print('Numero errado.')
            tentativas.append(1)
    except ValueError:
        print('ValueError: Digite apenas numeros inteiros.')

print('O Numero de tentativas foi', sum(tentativas))
