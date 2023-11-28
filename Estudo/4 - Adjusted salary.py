""" Fazer um algoritmo que ao receber o salário atual de um funcionário, 
calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
Salário atual	Reajuste
Abaixo de R$500,00	15%
de R$500,00 até R$1000,00	10%
Acima de R$1000,00	5% """

print('\t ==== Cálculo do salário reajustado ===')
salario_atual = float(input('Digite o salário atual: R$ '))

if (salario_atual < 500.00):
    salario_novo = salario_atual + (salario_atual * 0.15)
    print(f'Salario com reajuste = R${salario_novo}')

if (salario_atual >= 500.00):
    salario_novo = salario_atual + (salario_atual * 0.10)
    print(f'Salário com reajuste = R$ {salario_novo}')

if (salario_atual > 1000.00):
    salario_novo = salario_atual + (salario_atual * 0.10)
    print(f'Salário com reajuste = R$ {salario_novo}')

print('\t ====' * 10)