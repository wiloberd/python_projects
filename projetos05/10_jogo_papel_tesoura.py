import random
from time import sleep

mensagem = 'JOGO PAPEL TESOURA PEDRA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

lista = ['PEDRA', 'PAPEL', 'TESOURA']

computador_escolha = random.choice(lista)
jogador_escolha = ''

#print('Informe a forma de pagamento, escolhendo uma das opções abaixo..')

print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')

opcao = int(input('Faça sua escolha: '))
if opcao == 1:
    jogador_escolha = lista[0]
elif opcao == 2:
    jogador_escolha = lista[1]
elif opcao == 3:
    jogador_escolha = lista[2]
else:
    print('Opção invalida!')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')


print('-='*20) 
print(f'Escolha do Jogador {jogador_escolha}')
print(f'Escolha do computador {computador_escolha}')
if computador_escolha == 'PEDRA':
    if jogador_escolha == 'PEDRA':
        print('EMPATE')
    elif jogador_escolha == 'PAPEL':
        print('JOGADOR VENCE')
    elif jogador_escolha == 'TESOURA':
        print('COMPUTADOR VENCE')
elif computador_escolha == 'PAPEL':
    if jogador_escolha ==  'PEDRA':
        print('COMPUTADOR VENCE')
    elif jogador_escolha == 'PAPEL':
        print('EMPATE')
    elif jogador_escolha == 'TESOURA':
        print('JOGADOR VENCE')
elif computador_escolha == 'TESOURA':
    if jogador_escolha ==  'PEDRA':
        print('JOGADOR VENCE')
    elif jogador_escolha == 'PAPEL':
        print('COMPUTADOR VENCE')
    elif jogador_escolha == 'TESOURA':
        print('EMPATE')
print('-='*20) 

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 45: Crie um programa que faça 
o computador jogar Jokenpô com você.
"""