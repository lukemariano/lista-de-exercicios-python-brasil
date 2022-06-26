"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> eh_ano_bissexto(400)
    True
    >>> eh_ano_bissexto(800)
    True
    >>> eh_ano_bissexto(2100)
    False
    >>> eh_ano_bissexto(2004)
    True
    >>> eh_ano_bissexto(2022)
    False

"""


def eh_ano_bissexto(ano: int):
    """Escreva aqui em baixo a sua solução"""
    #passo 1: descobrir se ano / 4 tem o resto 0 ou se é multiplo de 400; se tiver, então o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(True)
    #passo 2: se não entrar nas condições acima, é falso
    else:
        print(False)   