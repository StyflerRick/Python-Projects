while True:
    try:
        numero = int(input('Digite um numero:'))
        if numero < 2:
            print('O número deve ser maior ou igual a 2.')
        else:
            eh_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                print(f'O número {numero} é primo.')
                break
            else:
                print(f'O número {numero} não é primo.')
    except ValueError:
        print('Value Error: Digite apenas números inteiros.')
