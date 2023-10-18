mensagem = 'CALCULADOR DE PREÇO DE PASSAGEM'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

distancia_informada = float(input('Informe a distancia da viagem em Km: '))

aviso_passagem = 'NORMAL: O preço da viagem passagem é R$0.50/Km, ' if distancia_informada <= 200 else 'PROMO: Para viagem de +200km, o preço é de R$0.45/km,'

# calcular preço da passagem utilizando operador ternario.
preco_passagem = distancia_informada * 0.50 if distancia_informada <= 200 else distancia_informada * 0.45

print('{} o preço total da sua passagem vai ficar R${:.2f}.'.format(aviso_passagem, preco_passagem) if distancia_informada <= 200  else '{} o preço total da sua passagem vai ficar R${:.2f}.'.format(aviso_passagem, preco_passagem))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 31: Desenvolva um programa que pergunte 
a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para 
viagens mais longas.
"""