from random import randint
from time import sleep

mensagem = 'MEGA SENA'
mensagem_final = ' ** BOA SORTE ** '
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)



lista_jogos = []

quantidade_jogo = int(input('Quantos palpites de jogos gostaria de criar: '))

for jogo in range(0, quantidade_jogo):
    jogo = []
    while len(jogo) < 6:
        numero_sorteado = randint(0, 60)
        if numero_sorteado not in jogo:
            jogo.append(numero_sorteado)
    lista_jogos.append(jogo)


for index, jogo in enumerate(lista_jogos):
    jogo.sort()
    print('Jogo {}: {}'.format((index + 1) , lista_jogos[index]))
    sleep(1)
        
print('*'*50)
print('{:^50}'.format(mensagem_final))
print('*'*50)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 088: Faça um programa que ajude um jogador 
da MEGA SENA a criar palpites.O programa vai perguntar quantos 
jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
cada jogo, cadastrando tudo em uma lista composta.
"""