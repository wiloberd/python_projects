mensagem = 'CAIXA ELETRONICA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

cedulas_cinquenta = 0
cedulas_vinte = 0
cedulas_cinco = 0
cedulas_um = 0

resto = 0

valor_informado = int(input('Qual é o valor que você deseja sacar: '))

if valor_informado >= 50:
    if (valor_informado % 50 == 0):
        cedulas_cinquenta = valor_informado / 50 
    else: 
        cedulas_cinquenta = valor_informado // 50
        resto = valor_informado % 50
    
    if resto != 0:
        if resto >= 20:
            if (resto % 20 == 0):
                cedulas_vinte = resto / 20 
            else: 
                cedulas_vinte = resto // 20
                resto = resto % 20

    if resto != 0:
        if resto >= 10:
            if (resto % 10 == 0):
                cedulas_cinquenta = resto / 10 
            else: 
                cedulas_cinquenta = resto // 10
                resto = valor_informado % 10

    if resto != 0:
        if resto >= 5:
            if (resto % 5 == 0):
                cedulas_cinco = resto / 5 
            else: 
                cedulas_cinco = resto // 5
                resto = valor_informado % 5
                
    if resto != 0:
        if resto < 5:
            if resto == 4:
                cedulas_um = 4
            elif resto == 3:
                cedulas_um = 3
            elif resto == 2:
                cedulas_um = 2
            else: 
                cedulas_um = 1
        



print('{:.0f} -> R$50'.format(cedulas_cinquenta))
print(' {:.0f} -> R$20'.format(cedulas_vinte))
print(' {:.0f} -> R$5 '.format(cedulas_cinco))
print(' {:.0f} -> R$1 '.format(cedulas_um))




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 071: Crie um programa que simule o 
funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado 
(número inteiro) e o programa vai informar quantas 
cédulas de cada valor serão entregues. 

OBS: considere que o caixa possui cédulas 
de R$50, R$20, R$5 e R$1.
"""