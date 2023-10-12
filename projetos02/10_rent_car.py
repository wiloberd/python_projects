# Exercício Python 15: Escreva um programa que pergunte a quantidade 
# de Km percorridos por um carro alugado e a quantidade de dias pelos 
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
# custa R$60 por dia e R$0,15 por Km rodado.
mensagem = 'RENT A CAR'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

quantidade_dias = int(input('Informe a quantidade de dias: '))

km_percorido = float(input('Informe a quantidade kilometro percorido: '))

# determinando separadamente cada custo e somando eles de acordo com as especificações.
valor_total = (quantidade_dias * 60) + (km_percorido * 0.15 )

print('''A quantidade de dias de uso do carro foi {}, 
com {}km percorido, o valor a pagar é R${:.2f} BRL.'''.format(quantidade_dias, 
km_percorido, valor_total))
