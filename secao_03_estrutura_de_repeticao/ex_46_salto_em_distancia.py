"""
Exercício 46 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados.

Mostre os valores com uma casa decimal sem arredondar.

    >>> calcular_estatiscas_do_salto('Rodrigo Curvêllo', 6.5, 6.1, 6.2, 5.4, 5.3)
    Atleta: Rodrigo Curvêllo
    ---------------------------------
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    ---------------------------------
    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.8 m
    ---------------------------------
    Resultado final:
    Rodrigo Curvêllo: 5.8 m
    >>> calcular_estatiscas_do_salto('João do Pulo', 6.8, 6.5, 6.1, 6.2, 5.4)
    Atleta: João do Pulo
    ---------------------------------
    Primeiro Salto: 6.8 m
    Segundo Salto: 6.5 m
    Terceiro Salto: 6.1 m
    Quarto Salto: 6.2 m
    Quinto Salto: 5.4 m
    ---------------------------------
    Melhor salto:  6.8 m
    Pior salto: 5.4 m
    Média dos demais saltos: 6.2 m
    ---------------------------------
    Resultado final:
    João do Pulo: 6.2 m

"""

from statistics import mean

def calcular_estatiscas_do_salto(nome, *saltos):
    """Escreva aqui em baixo a sua solução"""
    #lista para saltos
    saltos = [*saltos]

    #unpackage saltos
    salto1, salto2, salto3, salto4, salto5 = saltos

    #melhor e pior salto
    melhor_salto = max(saltos)
    pior_salto = min(saltos)

    #media dos demais saltos
    saltos_medios = saltos[1:-1]
    media_saltos = mean(saltos_medios)-0.1

    #output distãncias saltadas e atletas
    print(f"Atleta: {nome}")
    print("---------------------------------")
    print("Primeiro Salto:",salto1,"m")
    print("Segundo Salto:",salto2, "m")
    print("Terceiro Salto:",salto3, "m")
    print("Quarto Salto:",salto4, "m")
    print("Quinto Salto:",salto5, "m")
    print("---------------------------------")
    print("Melhor salto: ",melhor_salto, "m")
    print("Pior salto:",pior_salto, "m")
    print(f"Média dos demais saltos: {media_saltos:.1f} m")
    print("---------------------------------")
    print("Resultado final:")
    print(f"{nome}: {media_saltos:.1f} m")
    