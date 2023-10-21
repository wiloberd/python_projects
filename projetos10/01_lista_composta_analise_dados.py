mensagem = 'ANALISADOR DE DADOS'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

contador_numero = 0
lista_pessoas = []
lista_pessoa = []
maior = menor = 0
resposta = 'S'


while resposta == 'S':
    nome_informado = str(input(f'Digite o nome completo da pessoa: '))
    peso_informado = float(input(f'Digite o peso da pessoa: '))

    # identificando o maior e o menor peso
    if len(lista_pessoas) == 0:
        maior = peso_informado
        menor = peso_informado
    else:
        if peso_informado > maior:
            maior = peso_informado
        if peso_informado < menor:
            menor = peso_informado

    # inserindo cada grupo de dado na lista de pessoas
    lista_pessoa.append(nome_informado)
    lista_pessoa.append(peso_informado)
    lista_pessoas.append(lista_pessoa[:])
    lista_pessoa.clear()


    resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Informe uma resposta valida...')
        resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]

    if resposta == 'N':
        break



# Impressão final dos resutaldos
print('*'*50)
print(f'Ao todo foram {len(lista_pessoas)} pessoas cadastradas.')

print('Pessoa mais pesada é: ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end= ' ')


print('\nPessoa menos pesada é: ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end= ' ')
print('\n', end='')

print('*'*50)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 084: Faça um programa que leia nome e peso 
de várias pessoas, guardando tudo em uma lista. No final, 
mostre:                

A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
"""