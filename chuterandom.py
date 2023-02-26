import random
randomnum = random.randint(0, 10)  # Numero aleatorio de 0 a 10
randomnum = int(randomnum)  # Define variavel como 'int'
print('Numero aleatorio é {}'.format(randomnum))


def chute():
    global randomnum
    while True:
        # Solicita ao usuario um numero de 0 a 10.
        varchute = input('Chute um numero de 0 a 10:')
        varchute = int(varchute)  # Define a variavel como 'int'
        if varchute == randomnum:
            print('Parabens, você acertou.')
            break
        elif varchute > randomnum:
            print('Chutou alto demais, tente um numero menor')

        else:
            varchute < randomnum
            print('Chutou baixo demais, tente um numero maior')


chute()
