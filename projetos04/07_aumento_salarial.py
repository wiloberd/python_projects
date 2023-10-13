mensagem = 'AUMENTO SALARIAL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

salario_funcionario = float(input('Informe o salario do funcionario: '))

aumento_salarial = 0

if (salario_funcionario > 1250):
    percentagem = (salario_funcionario * 10)/100
    aumento_salarial = salario_funcionario + percentagem 
elif(salario_funcionario <= 1250):
    percentagem = (salario_funcionario * 15)/100
    aumento_salarial = salario_funcionario + percentagem 

print('O salario do funcionário passará de R${} para R${}, adicionando uma percentagem de 10%.'.format(salario_funcionario, aumento_salarial) if salario_funcionario > 1250 else 'O salario do funcionário passará de {} para {}, adicionando uma percentagem de 15%.'.format(salario_funcionario, aumento_salarial))

print(f'O valor acrescentado foi: R${percentagem}')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 34: Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento. Para salários superiores 
a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
o aumento é de 15%.

"""