from datetime import date

mensagem = 'ANO BISSEXTO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

ano_informado = int(input('Digite 0 para verificar o ano atual ou Informe o ano: '))

if ano_informado == 0:
    ano_informado = date.today().year


# verificação do ano, sabendo que um ano é bissexto se é divisivel por 4, 
# e multiplo de 100 qua não são multiplo de 400
if( ano_informado % 4 == 0 and ano_informado % 100 != 0 or ano_informado % 400 == 0 ):
    bissexto = True
else:
    bissexto = False

mensagem = 'é um ano bissexto' if (bissexto) else 'não é um ano bissexto.'
print('{} {}'.format(ano_informado, mensagem))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 32: Faça um programa que leia um ano 
qualquer e mostre se ele é bissexto.
"""