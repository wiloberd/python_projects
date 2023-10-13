
numero_informado = int(input('Informe um numero entre 0-9999: '))
unidade = numero_informado    // 1 % 10
dezena  = numero_informado   // 10 % 10
centena = numero_informado  // 100 % 10
milhar  = numero_informado // 1000 % 10

print('Unidade: {}  '.format(unidade))
print('Dezenas: {}  '.format(dezena))
print('Centenas: {} '.format(centena))
print('Milhar: {}   '.format(milhar))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 23: Faça um programa que leia um número 
de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""