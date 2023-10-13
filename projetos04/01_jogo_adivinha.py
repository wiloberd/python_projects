import random
from time import sleep
mensagem = 'JOGO ADIVINHA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

numero_gerado = random.randint(0, 5)

#print(numero_gerado)
numero_informado = int(input('Qual é o numero que vai ser sorteado pelo computador: '))


# utilizando operador ternário em python
resposta ='ACERTOUU!'if numero_gerado == numero_informado else 'ERROUUU...'

print('Processando...')
sleep(2)

print('*'*40)
print('{}, o numero sorteado foi {} dessa vez! '.format(resposta, numero_gerado))

print('Na proxima vez com certeza tu vai acertar!' if numero_gerado != numero_informado else 'PARABÉNS')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” 
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
qual foi o número escolhido pelo computador. O programa deverá escrever 
na tela se o usuário venceu ou perdeu.

"""