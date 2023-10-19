mensagem = 'PROGRESSÃO ARITMETICA V2.0'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

progressao = 0
contador = 0

inicio_intervalo = int(input('Informe o primeiro termo: '))
progressao_aritmetica = int(input('Informe a progressão aritmetica: '))


while contador < 10:
    if progressao == 0:
        progressao = inicio_intervalo
    else:
        progressao =  progressao + progressao_aritmetica 

    print('{} -> '.format(progressao), end= '')
    contador += 1

print('FIM')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo 
e a razão de uma PA, mostrando os 10 primeiros termos da progressão 
usando a estrutura while.
"""