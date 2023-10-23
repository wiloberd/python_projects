mensagem = 'PRINT ESPECIAL'

def cabecalho(mensagem):
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)



def print_especial(texto_informado):
    tamanho_texto = len(texto_informado) + 4
    print('*'*tamanho_texto)
    print('  {}'.format(texto_informado))
    print('*'*tamanho_texto)



cabecalho(mensagem)

texto_informado = 'JOGADOR DE FUTEBOL'
print_especial(texto_informado)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 097: Faça um programa que tenha uma função 
chamada escreva(), que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.                                  
Ex: escreva('Olá, Mundo!') 

Saída:
   ~~~~~~~~~~~
   Olá, Mundo!
   ~~~~~~~~~~~ 
"""