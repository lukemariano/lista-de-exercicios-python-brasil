"""
Exercício 44 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


    >>> apurar_votos('1')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1     100.0%
    2                   Luladrão          0       0.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      50.0%
    2                   Luladrão          1      50.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      33.3%
    2                   Luladrão          1      33.3%
    3                   Dilmanta          1      33.3%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      25.0%
    2                   Luladrão          1      25.0%
    3                   Dilmanta          1      25.0%
    4                   FHC Isentão       1      25.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      20.0%
    2                   Luladrão          1      20.0%
    3                   Dilmanta          1      20.0%
    4                   FHC Isentão       1      20.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      20.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      16.7%
    2                   Luladrão          1      16.7%
    3                   Dilmanta          1      16.7%
    4                   FHC Isentão       1      16.7%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      16.7%
    6                   Votos Brancos     1      16.7%
    >>> apurar_votos('1', '2', '3', '4', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1       5.6%
    2                   Luladrão          1       5.6%
    3                   Dilmanta          1       5.6%
    4                   FHC Isentão       1       5.6%
    -------------------------------------------------------------------
    5                   Votos Nulos       7      38.9%
    6                   Votos Brancos     7      38.9%


"""
from collections import Counter


def apurar_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    votos = [*votos]
    bostonaro = 0
    luladrao = 0
    dilmanta = 0
    fhc = 0
    nulo = 0
    branco = 0
    
    for i in range(len(votos)):
        if votos[i] == "1":
            bostonaro += 1
        if votos[i] == "2":
            luladrao += 1
        if votos[i] == "3":
            dilmanta += 1
        if votos[i] == "4":
            fhc += 1
        if votos[i] == "5":
            nulo += 1
        if votos[i] == "6":
            branco += 1
        i+=1

    total_votos = bostonaro + luladrao + dilmanta + fhc + nulo + branco 
    porcentagem_bostonaro = (bostonaro * 100) / total_votos
    porcentagem_luladrao = (luladrao * 100) / total_votos
    porcentagem_dilmanta = (dilmanta * 100) / total_votos
    porcentagem_fhc = (fhc * 100) / total_votos
    porcentagem_nulo = (nulo * 100) / total_votos
    porcentagem_branco = (branco * 100) / total_votos

    print("Código do Candidato Nome do Candidato Votos Porcentagem sobre total")
    print(f"1                   Bostonaro         {bostonaro}{porcentagem_bostonaro:10.1f}%")
    print(f"2                   Luladrão          {luladrao}{porcentagem_luladrao:10.1f}%")
    print(f"3                   Dilmanta          {dilmanta}{porcentagem_dilmanta:10.1f}%")
    print(f"4                   FHC Isentão       {fhc}{porcentagem_fhc:10.1f}%")
    print("-------------------------------------------------------------------")
    print(f"5                   Votos Nulos       {nulo}{porcentagem_nulo:10.1f}%")
    print(f"6                   Votos Brancos     {branco}{porcentagem_branco:10.1f}%")
