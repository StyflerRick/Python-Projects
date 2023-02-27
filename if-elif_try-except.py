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
            print("O resultado é:", result)
        except ZeroDivisionError:
            print("A lista não pode ser vazia.")
        except TypeError:
            print("A lista contém elementos que não podem ser somados.")


# Teste da função com diferentes dados
process_data(None)
process_data("teste")
process_data([12, 56])
process_data([1, 2, 3])
process_data([1, 2, "teste"])
