mensagem = 'NUMEROS PRIMOS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

numero_informado = int(input('Informe um numero: '))

if ( numero_informado > 0 and numero_informado % 2 != 0):
    print(f'-> {numero_informado} é um numero primo.')
else:
    print(f'-> {numero_informado} não é um numero primo.')

print('*'*40)

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 52: Faça um programa que leia um número 
inteiro e diga se ele é ou não um número primo.
"""