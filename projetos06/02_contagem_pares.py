from time import sleep

mensagem = 'NUMERO PAR!!'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

for posicao in range(0, 51):
    if (posicao % 2 == 0 ):
        print(f'{posicao} - é par:')
        sleep(1)

print('FIM DO INTERVAL!')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 47: Crie um programa que mostre 
na tela todos os números pares que estão no 
intervalo entre 1 e 50.
"""