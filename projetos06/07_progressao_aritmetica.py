mensagem = 'PROGRESSÃO ARITMETICA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)


inicio_intervalo = int(input('Informe o primeiro termo: '))
progressao_aritmetica = int(input('Informe a progressão aritmetica: '))
progressao = 0

fim_intervalo = inicio_intervalo + 10


for posicao in range(inicio_intervalo, fim_intervalo):
    if progressao == 0:
        progressao = inicio_intervalo
    else:
        progressao =  progressao + progressao_aritmetica 

    print('{} -> '.format(progressao), end= '')

print('FIM')
    

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 51: Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.
"""