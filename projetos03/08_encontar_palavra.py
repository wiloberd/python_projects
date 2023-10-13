cidade_informada = str(input('Informe a cidade que você nasceu: '))

input_tratado = cidade_informada.upper()
palavra = 'RIO'

print('A cidade informada começa com rio na sua escrita? : {} '.format(input_tratado[:3] == palavra))

print('A cidade informada contém rio na sua escrita? : {} '.format(palavra in input_tratado))

"""
Exercício Python 24: Crie um programa que leia o nome 
de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""