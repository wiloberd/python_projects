import random
from time import sleep
mensagem = 'JOGO ADIVINHA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

numero_gerado = random.randint(0, 10)
numero_informado = int(input('Qual é o numero que vai ser sorteado pelo computador: '))
tentativa = 1

while numero_gerado != numero_informado:
    print('Processando...')
    sleep(1)
    print(f'Errouu! o numero foi {numero_gerado}!')
    # gerando um novo numero
    numero_gerado = random.randint(0, 10)
    numero_informado = int(input('Informe um novo numero: '))
    tentativa += 1

# utilizando operador ternário em python
resposta ='ACERTOUU!'

print('Processando...')
sleep(2)

print('*'*40)
print('{}, o numero sorteado foi {} dessa vez! '.format(resposta, numero_gerado))
print('Você acertou na {}º tentativa.'.format(tentativa))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador 
vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai 
tentar adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.
"""