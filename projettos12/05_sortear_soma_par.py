from time import sleep
from random import randint

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


valores = []

def sortear():
    for n in range(0, 5):
        n = randint(0, 10)
        valores.append(n)
    print(f'\033[0;32m A lista dos valores seteados: {valores} \033[m')



def soma(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
        else:
            pass
    print(f'\033[0;32mO soma dos valores par é: {soma}\033[m')







mensagem = 'SORTEAR E SOMA PAR'
cabecalho(mensagem)
separador('SORTEANDO OS VALORES')
sortear() 

separador('SOMA DOS VALORES PAR')
soma(valores)
rodape()



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 100: Faça um programa que tenha uma lista chamada 
números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da 
lista e a segunda função vai mostrar a soma entre todos os valores 
pares sorteados pela função anterior.
"""