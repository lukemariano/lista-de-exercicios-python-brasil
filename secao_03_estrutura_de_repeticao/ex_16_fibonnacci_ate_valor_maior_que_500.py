"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
 valor seja maior que 500.

    >>> calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500()
    '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610'
"""


def calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500() -> str:
    """Escreva aqui em baixo a sua solução"""
    n = 15
    fibonacci = [1, 1]
    cont = 0
    if n == 1:
        print("'1'")
    else:
        while cont < n - 2:
            fibonacci += [fibonacci[cont] + fibonacci[cont + 1]]
            cont += 1
        else:
            print("'0, ", end = '')
            print(*fibonacci, sep = ', ', end = '')
            print("'", end = '')
