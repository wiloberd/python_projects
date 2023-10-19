mensagem = 'SUPER PROGRESSÃO ARITMETICA V3.0'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)


progressao = 0
contador = 0
quantidade_termos = 10
total_termos_gerado = 0
resposta = 'S'

inicio_intervalo = int(input('Informe o primeiro termo: '))
progressao_aritmetica = int(input('Informe a progressão aritmetica: '))


while resposta == 'S':
    total_termos_gerado = total_termos_gerado + quantidade_termos
    while contador < quantidade_termos:

        if progressao == 0:
            progressao = inicio_intervalo
        else:
            progressao =  progressao + progressao_aritmetica 

        print('{} -> '.format(progressao), end= '')
        
        contador += 1

    print('PAUSA')

    resposta = str(input('Gostaria de mostrar mais alguns termos (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Resposta invalida!')
        resposta = str(input('Gostaria de mostrar mais alguns termos (S/N): ')).upper().strip()[0]
    if resposta == 'N':
        print('FIM')
    else:
        contador = 0
        quantidade_termos = int(input('Quantos termos a mais deseja mostrar: '))

print('\033[0;32m*'*40)
print('Ao todo foi gerado {} termos.'.format(total_termos_gerado))
print('*'*40, end='\033[m')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando 
para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""