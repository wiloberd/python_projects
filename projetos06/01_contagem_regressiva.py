from time import sleep

mensagem = 'CONTAGEM REGRESSIVA!!'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

tempo = 11

for posicao in range(0, 11):
    tempo = tempo - 1
    print(tempo)
    sleep(1)

print('FELIZ ANO NOVO!!!')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 46: Faça um programa que mostre na tela 
uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""