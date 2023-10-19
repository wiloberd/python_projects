from random import randint


valor_usuario = int(input('Informe o seu valor: '))
valor_computador = randint(0, 11)
jogador_vitorias = 0
total = valor_computador + valor_usuario


while True:
    paridade = str(input('Quer um valor PAR ou IMPAR: ')).upper().strip()[0]
    print('Você jogou {} o computador {} e o resultado deu {}.'.format(valor_usuario, valor_computador, total))
    print('é PAR' if total % 2 == 0 else 'é IMPAR')
    while paridade not in 'PI':
        paridade = str(input('Informe novamente a paridade deve ser (P/I): ')).upper().strip()[0]

    if (paridade == 'P' and total % 2 ==0):
        print('Você ganhou!!')
        jogador_vitorias =+ 1
        valor_usuario = int(input('Informe um novo valor: '))
    elif (paridade == 'I' and total % 2 != 0):
        print('Você ganhou!!')
        jogador_vitorias =+ 1
        valor_usuario = int(input('Informe um novo valor: '))
    else:
        print('Você perdeuu!')
        break

print(f'GAME OVER!  Você ganhou {jogador_vitorias}')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 68: Faça um programa que jogue par ou 
ímpar com o computador. O jogo só será interrompido 
quando o jogador perder, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo.
"""