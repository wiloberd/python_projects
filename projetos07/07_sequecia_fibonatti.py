mensagem = 'PROGRESSÃO ARITMETICA V2.0'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

valor_atual = 0
progressao = 0
contador = 0
valor_anterior = 1

ultimo_termo = int(input('Informe o primeiro termo: '))

while contador < ultimo_termo:
    if contador <= 1:
        print('{} ->'.format(contador), end= ' ')
        contador += 1
    else:    
        progressao = valor_anterior + valor_atual
        print('{} -> '.format(progressao), end= ' ')
        contador += 1
        valor_atual = valor_anterior
        valor_anterior = progressao
    

print('FIM')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 63: Escreva um programa que leia um 
número N inteiro qualquer e mostre na tela os N primeiros 
elementos de uma Sequência de Fibonacci. Exemplo:

    
0 - 1 - 1 - 2 - 3 - 5 - 8  <<<<<
"""