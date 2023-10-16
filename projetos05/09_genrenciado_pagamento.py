mensagem = 'GENRENCIADOR DE PAGAMENTO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

valor_informado = int(input('Informe o valor do produto: '))
novo_preco = 0

print('Informe a forma de pagamento, escolhendo uma das opções abaixo..')

print('''
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão 
[4] 3x ou mais no cartão 
      ''')

opcao = int(input('Informe a opção: '))

if ( opcao == 1 ):
    desconto = valor_informado * 10 / 100
    novo_preco = valor_informado - desconto
    print('Você ganhou 10% de desconto')
    print('O valor a ser pago R${:.2f}'.format(novo_preco)) 
elif ( opcao == 2 ):
    desconto = valor_informado * 5 / 100
    novo_preco = valor_informado - desconto
    print('Você ganhou 5% de desconto')
    print('O valor a ser pago R${:.2f}'.format(novo_preco)) 
elif ( opcao == 3 ):
    print('Você pagará o produto no seu valor normal')
    print('O valor a ser pago R${:.2f}'.format(valor_informado)) 
elif ( opcao == 4 ):
    juros = valor_informado * 20 / 100
    novo_preco = valor_informado + juros
    print('Você pagará o produto no seu com 20% de juros')
    print('O valor a ser pago R${:.2f}'.format(novo_preco)) 
else:
    print('Opção invalida.')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 44: Elabore um programa que calcule o 
valor a ser pago por um produto, considerando o seu 
preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal 
- 3x ou mais no cartão: 20% de juros
"""