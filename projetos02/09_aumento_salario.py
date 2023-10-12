# Este programa calcula e aplique aumento em salario de funcionário.
mensagem = 'CALCULADOR DE AUMENTO SALARIAL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

salario_funcionario = float(input('Digite o salario do funcionário: '))

# calculando o valor do aumento.
aumento = (salario_funcionario * 15) / 100

# aplicando o aumento no salario antigo.
novo_salario_funcionario = salario_funcionario + aumento 

print('O funcionário receberá um valor de R${:.2f} BRL de aumento, e seu novo salario será R${:.2f} BRL'.format(aumento, novo_salario_funcionario))