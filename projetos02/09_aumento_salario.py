# Este programa calcula e aplique aumento em salario de funcionário.
mensagem = 'CALCULADOR DE AUMENTO SALARIAL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

salario = float(input('Digite o salario do funcionário: '))

# calculando o valor do aumento.
aumento = (salario * 15) / 100

# aplicando o aumento no salario antiga.
novo_salario = salario + aumento 

print('O funcionário receberá um valor de R${:.2f} BRL de aumento, e seu novo salario será R${:.2f} BRL'.format(aumento, novo_salario))