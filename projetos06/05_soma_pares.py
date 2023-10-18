mensagem = 'SOMA PAR!!'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

soma = 0

for posicao in range(0, 6):
    numero = int(input(f'Digite o {posicao + 1}º numero: '))
    if (numero % 2 == 0):        
        soma = numero + soma
print(f'O resultado da soma deu {soma}.')

print('*'*40)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 50: Desenvolva um programa que leia seis 
números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.
"""