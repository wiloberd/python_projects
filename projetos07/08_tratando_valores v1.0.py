mensagem = 'CONTADOR DE NUMEROS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

soma_numeros = tentativa = 0

numero_informado = int(input('Informe um numero ou [999] para o programa: '))

while numero_informado != 999:
    soma_numeros = soma_numeros + numero_informado
    tentativa += 1
    
    numero_informado = int(input('Informe um numero ou [999] para o programa: '))

print('Quantidade de numero informado foi {} e a soma de todos os numeros informado foi {}'.format(tentativa, soma_numeros))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 64: Crie um programa que leia vários números 
inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No final, mostre 
quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag).
"""