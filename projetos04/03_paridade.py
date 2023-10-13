mensagem = 'PARIDADE DE NUMERO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

numero_informado = int(input('Me diga um numero e eu te digo se é par ou impar: '))


resposta = 'é um numero PAR!' if ((numero_informado % 2) == 0) else 'é um numero IMPAR!'

print('{} {}'.format(numero_informado, resposta))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 30: Crie um programa que leia um número 
inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""