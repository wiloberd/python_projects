from time import sleep
mensagem = 'EMPRESTIMO FACÍL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

valor_imovel = float(input("Informe o valor do Imovél: "))
salario_requerente= float(input('Informe seu salario liquido: '))

# prazo do reembolso deve ser informado em ano.
prazo_ano = int(input('Informe o periodo de tempo em que pretende reembolsar o valor: '))

# melhor lógica para determinar  parcela mensal
parcela_mensal = valor_imovel / (prazo_ano * 12 )

# logica alternativa não muito explicito
#parcela_mensal = (valor_imovel /  prazo_ano ) / 12

# calculando a percentagem de 30% do salario
percentagem_salario = (salario_requerente * 30) / 100

print('Processando...')
sleep(2)
# logica para determinar o valor mensal das parcelas.
if (parcela_mensal > percentagem_salario):
    print('Infelizmente você não está aprovado...')
    print('Razão: O valor das parcelas serão R${:.2f}/mês em {} anos.'.format(parcela_mensal ,prazo_ano))
else:
    print('Excelente! você está aprovado.')
    print('CONTRATO: o valor de cada parcela será de R${:.2f} por mês.'.format(parcela_mensal))
    sleep(2)
    print(f'Obrigado por contar com o team {mensagem}' )



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo 
bancário para a compra de uma casa. Pergunte o valor da casa, o salário 
do comprador e em quantos anos ele vai pagar. A prestação mensal não 
pode exceder 30% do salário ou então o empréstimo será negado.
"""