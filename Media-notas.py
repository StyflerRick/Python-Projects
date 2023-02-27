def process_data(data):
    if data is None:
        print("Nenhum dado foi fornecido.")
    elif not isinstance(data, list):
        print("Os dados devem ser fornecidos em uma lista.")
    elif len(data) == 0:
        print("A lista está vazia.")
    else:
        try:
            # Processamento dos dados
            result = sum(data) / len(data)
            print('A media de notas desse aluno é', result)
        except ZeroDivisionError:
            print("A lista não pode ser vazia.")
        except TypeError:
            print("A lista contém elementos que não podem ser somados.")
        except ValueError:
            print('Os valores devem ser em numeros.')


notas = []
for i in range(4):
    while True:
        try:
            nota = float(input(f"Digite a {i+1}ª nota:"))
            notas.append(nota)
            break
        except ValueError:
            print("Valor inválido. Digite um número.")

process_data(notas)