
frase_informado = str(input('Informe uma frase: '))

print('A letra a apereceu {} vezes'.format(frase_informado.upper().count('A')))

print('A primeira occorência apereceu na posição {}'.format(frase_informado.strip().upper().find('A') + 1))

print('A última occorência apereceu na posição {}'.format(frase_informado.strip().upper().rfind('A') + 1))




"""
Exercício Python 26: Faça um programa que leia uma 
frase pelo teclado e mostre quantas vezes aparece 
a letra “A”, em que posição ela aparece a primeira 
vez e em que posição ela aparece a última vez.
"""