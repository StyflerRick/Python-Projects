import tkinter as tk
import Cotas


# Cores
cor_preto = "#3b3b3b"  # Preto
cor_branco = "#ffffff"  # Branco
cor_azul = "#38576b"  # Azul
cor_cinza = "#ECEFF1"  # Cinza
cor_laranja = "#FFAB40"  # Laranja

root = tk.Tk()
root.title('Cotações Atuais')
frame = tk.Frame(root)


def BuscarCotas():
    global DolarCota
    global BTCCota
    Cotas.dolar_reais()
    Cotas.BTC_Real()
    BTCCota = Cotas.BTCCota
    DolarCota = Cotas.DolarCota


BuscarCotas()


colunas = ['Moeda', 'Valor em Real']
dados = [['Dolar', f'$1 = R${DolarCota:.2f}'], [
    'BTC', f'1 BTC = R${BTCCota:.2f}'], ['', '']]


for i, coluna in enumerate(colunas):
    tk.Label(frame, text=coluna, padx=10, pady=10).grid(row=0, column=i)

for i, linha in enumerate(dados):
    for j, valor in enumerate(linha):
        tk.Label(frame, text=valor, padx=10, pady=10).grid(row=i+1, column=j)


def atualizar_tabela():
    global DolarCota
    global BTCCota
    BuscarCotas()
    # leia novos dados do banco de dados ou de uma API
    novos_dados = [['Dolar', '$1 = R${}'.format(DolarCota)], [
        'BTC', '1 BTC = R${}'.format(BTCCota)], ['', '']]

    # atualize os dados da tabela
    for i, linha in enumerate(novos_dados):
        for j, valor in enumerate(linha):
            tabela[i][j] = valor


tabela = []
for i, linha in enumerate(dados):
    tabela.append([])
    for j, valor in enumerate(linha):
        label = tk.Label(frame, text=valor, padx=10, pady=10)
        label.grid(row=i+1, column=j)
        tabela[i].append(label)

# Posiciona o botão abaixo da tabela na segunda linha
botao_atualizar = tk.Button(root, text='Atualizar', command=atualizar_tabela)
botao_atualizar.grid(row=3, column=0, pady=0)


frame.grid()
root.mainloop()
