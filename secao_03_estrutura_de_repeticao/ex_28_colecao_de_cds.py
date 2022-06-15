"""
Exercício 28 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

Mostre os valores monetórios com duas casas decimais..

    >>> from secao_03_estrutura_de_repeticao import ex_28_colecao_de_cds
    >>> entradas = ['1', '1']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 1
    Valor total da coleção: R$ 1.00
    Custo médio dos cds: R$ 1.00
    >>> entradas = ['40', '40', '2']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 2
    Valor total da coleção: R$ 80.00
    Custo médio dos cds: R$ 40.00
    >>> entradas = ['10', '20', '30', '40', '4']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 4
    Valor total da coleção: R$ 100.00
    Custo médio dos cds: R$ 25.00
    >>> entradas = ['10', '20', '30', '3']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 3
    Valor total da coleção: R$ 60.00
    Custo médio dos cds: R$ 20.00

"""


def calcular_estatisticas_colecao_de_cd():
    """Escreva aqui em baixo a sua solução"""
    #declarando lista para armazenar o preço unitário de cada CD
    valor_unitario = []
    #declarando input para receber a quantidade de CDs
    qtd_cds = int(input("Digite a quantidade de CDs: "))
    #loop para adicionar o preço unitário dos CDs a lista
    for i in range(0, qtd_cds):
        preco_cd = float(input("Digite o preço de cada CD: "))
        valor_unitario.append(preco_cd)
    #Operações matemáticas
    valor_total = sum(valor_unitario)
    valor_medio = valor_total/qtd_cds
    #output
    print(f"Número de cds: {qtd_cds}")
    print(f"Valor total da coleção: R$ {valor_total:.2f}")
    print(f"Custo médio dos cds: R$ {valor_medio:.2f}")

    





