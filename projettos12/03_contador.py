from time import sleep

def cabecalho(mensagem):
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)

def separador(texto):
    print('-'*50)
    print('{:^50}'.format(texto))

def rodape():
    mensagem = 'FIM DO PROGRAMA'
    print('*'*50)
    print('{:^50}'.format(mensagem))
    print('*'*50)


def contagem():
    separador('<-- Contagem Progressiva -->')
    for passo in range(1, 11):
        print(f'{passo}', end=' ', flush=True)
        sleep(1)
    print('FIM!')


    separador('<-- Contagem Regressiva -->')
    for passo in range(0, 12, 2):
        print(f'{10 - passo}', end=' ', flush=True)
        sleep(1)
    print('FIM!')

   
    separador('<-- Contagem Personalizada -->')
    inicio = int(input('Informe o inicio da contagem: '))
    fim = int(input('Informe o fim da contagem: '))
    progressao = int(input('Informe o passo: '))

    if progressao < 0:
        for passo in range(inicio, (fim - 1), progressao):
            print(f'{passo}', end=' ', flush=True)
            sleep(1)
        print('FIM!')
    elif progressao > 0:
        for passo in range(inicio, (fim + 1), progressao):
            print(f'{passo}', end=' ', flush=True)
            sleep(1)
        print('FIM!')
    elif progressao == 0:
        print('Ordem de progressão não pode ser zero (0)')


# chamada das funções
mensagem = 'CONTAGEM PERSONALIZADA'
cabecalho(mensagem)
contagem()
rodape()



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 098: Faça um programa que tenha uma função 
chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2 
c) uma contagem personalizada
"""