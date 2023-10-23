from time import sleep

def cabecalho(mensagem):
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)


def rodape():
    mensagem = 'FIM DO PROGRAMA'
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)


def maior(*value):
    maior = 0
    for lista in value:
        print('Analisando os valores passasdo...')
        sleep(1)
        print(f'Foram informado os valores seguintes: ', end='')
        
        for index, numero in enumerate(lista):
            print(numero, end=' ')
            if index == 0:
                if numero != 0:
                    maior = numero
                else:
                    pass
            else:
                if maior < numero:
                    maior = numero
        print(f'\nAo todo foram {len(lista)} ')
    sleep(2)
    print(f'O maior valor é: {maior}')
    sleep(1)



valores = [2, 9, 4, 5, 7, 1]



mensagem = 'IDENTIFICADOR DO MAIOR VALOR'
cabecalho(mensagem)
maior(valores)
rodape()


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 099: Faça um programa que tenha uma função 
chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles 
é o maior.
"""