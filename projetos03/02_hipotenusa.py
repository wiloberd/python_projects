from math import pow, sqrt, hypot

mensagem = 'CALCULADOR DE HIPOTENUSA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)
cateto_oposto = float(input('Informe o cateto oposto do triangulo: '))
cateto_adjacente = float(input('Informe o cateto ajdencente do triangulo: '))

hipotenusa = sqrt((pow(cateto_oposto,2) + pow(cateto_adjacente,2)))

# usando função hypot da biblioteca math
hipotenusa_built_in = hypot(cateto_oposto, cateto_adjacente)
print('*'*40)
print('O comprimento do triangulo {}x{} é igual a: {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))

print('O comprimento do triangulo {}x{} é igual a: {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa_built_in))

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 17: Faça um programa que leia o comprimento 
do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.
"""