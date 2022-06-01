"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato ( 5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""


def calcular_assalto_no_salario():
    """Escreva aqui em baixo a sua solução"""
    #1º passo: input quanto você ganha por hora e o número de horas trabalhadas no mês.
    salario_hora = float(input("Digite o salário por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    #2º passo: declarar variáveis: salário_bruto, ir, inss, sindicato e salario_liquido
    salario_bruto = salario_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - (ir + inss + sindicato)
    #3º passo: imprimir variáveis com duas casas decimais;
    print (f"+ Salário Bruto : {salario_bruto:.2f}\n- IR (11%) : R$ {ir:.2f}\n- INSS (8%) : R$ {inss:.2f}\n- Sindicato ( 5%) : R$ {sindicato:.2f}\n= Salário Liquido : R$ {salario_liquido:.2f}")