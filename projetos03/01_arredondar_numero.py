#importação do metodo floor da biblioteca math.
from math import floor, trunc, ceil

numero_informada = float(input('Informe um numero real: '))

# apenas corta a parte inteira
print(f'O numero que você informou foi {numero_informada}, e ficou {trunc(numero_informada)} após arredondar ele.')


# OUTRAS FUNÇÕES SIMILAR DA BIBLIOTECA MATH
# função ceil arredonda sempre para cima, sendo assim se o valor for
# negativo o valor será arredondado mais mais perto do zero, caso contrário
# mais longe do zero.
print(f'O numero que você informou foi {numero_informada}, e ficou {ceil(numero_informada)} após arredondar ele para cima.')

# função floor arredonda sempre para baixo, sendo assim se o valor for
# negativo o valor será arredondado mais mais longe do zero, caso contrario
# mais perto do zero.
print(f'O numero que você informou foi {numero_informada}, e ficou {floor(numero_informada)} após arredondar ele para baixo.')

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 16: Crie um programa que leia um número 
Real qualquer pelo teclado e mostre na tela a sua 
porção Inteira.

"""