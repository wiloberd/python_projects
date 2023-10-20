from random import randint

mensagem = 'MAIOR-MENOR VALOR'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)


tupla_valor = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10) )

maior_valor = 0
menor_valor = 0

for index, element in enumerate(tupla_valor):
    if index == 0:
        maior_valor = tupla_valor[index]
        menor_valor = tupla_valor[index]
    else:
        if tupla_valor[index] > maior_valor:
            maior_valor = tupla_valor[index]
        elif tupla_valor[index] < menor_valor:
            menor_valor = tupla_valor[index]

print('Maior valor igual a {}'.format(maior_valor))
print('Menor valor igual a {}'.format(menor_valor))



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 074: Crie um programa que vai gerar 
cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão na tupla.
"""