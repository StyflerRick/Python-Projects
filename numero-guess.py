import random

tentativas = [1]
randomnum = random.randint(0, 10)  # Numero aleatorio de 0 a 100
randomnum = int(randomnum)  # Define variavel como 'int'

while True:
    try:
        chute = int(input('Chute um numero de 0 a 10: '))
        if chute == randomnum:
            print('Você acertou o numero.')
            print('O Numero de tentativas foi', sum(tentativas))
            break
        elif chute > 10:
            print('Somente numeros entre 0 e 10.')
            tentativas.append(1)
            print(f'{sum(tentativas)}ª tentativa')
        else:
            print('Numero errado.')
            tentativas.append(1)
            print(f'{sum(tentativas)}ª tentativa')
    except ValueError:
        print('ValueError: Digite apenas numeros inteiros.')
