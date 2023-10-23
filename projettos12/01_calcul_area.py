mensagem = 'APROVEITAMENTO JOGADOR V2.0'

def cabecalho(mensagem):
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)

def rodape():
    mensagem = 'FIM DO PROGRAMA'
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)



def calcul_area():
    largura = float(input('Informe a largura do terreno (m): '))
    comprimento = float(input('Informe o comprimento do terreno (m): '))

    area_terreno = largura * comprimento

    print(f'A area do triangulo {largura}x{comprimento} m é : {area_terreno}m')



cabecalho(mensagem)
calcul_area()
rodape()


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 096: Faça um programa que tenha uma 
função chamada área(), que receba as dimensões de um terreno 
retangular (largura e comprimento) e mostre a área do terreno.
"""