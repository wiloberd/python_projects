mensagem = 'SOMA IMPAR!!'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

soma = 0

for posicao in range(1, 500):
    if (posicao % 2 != 0 and posicao % 3 == 0):        
        soma = posicao + soma
print(f'O resultado da soma deu {soma}')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 48: Faça um programa que calcule a soma 
entre todos os números que são múltiplos de três e que se 
encontram no intervalo de 1 até 500.
"""