mensagem = 'CADASTRO PESSOAS'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


dicionario_pessoas = {}
lista_pessoas = []
lista_mulheres = []
lista_pessoas_sup_media = []
soma_idade = 0
resposta = 'S'

while resposta == 'S':
    # lendo os valores do jogador
    nome_informado = str(input('Informe o nome completo da pessoa: '))
    sexo_informada = str(input('Informe o sexo da pessoa: ')).upper().strip()[0]
    idade_informada = int(input('Informe a idade da pessoa: '))

    dicionario_pessoas['nome'] = nome_informado
    dicionario_pessoas['sexo'] = sexo_informada
    dicionario_pessoas['idade'] = idade_informada

    lista_pessoas.append(dicionario_pessoas.copy())

    resposta = str(input('Deseja adicionar mais pessoas na lista (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Informe uma resposta valida...')
        resposta = str(input('Deseja adicionar mais pessoas na lista (S/N): ')).upper().strip()[0]

    if resposta == 'N':
        break

# media idade do grupo
for pessoa in lista_pessoas:
    soma_idade = soma_idade + pessoa['idade']

media_idade = soma_idade / len(lista_pessoas)


# lista das mulheres
for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'F':
        lista_mulheres.append(pessoa)
    else:
        pass

# lista das pessoas acima da idade media
for pessoa in lista_pessoas:
    if pessoa['idade'] > media_idade:
        lista_pessoas_sup_media.append(pessoa)
    else:
        continue


print('*'*50)
print(f'Ao todo foram cadastrados {len(lista_pessoas)} pessoas.')
print('A média de idade do grupo é : {:.2f} anos.'.format(media_idade))
print(f'A lista de nome das mulheres cadastradas: {lista_mulheres}.')
print(f'A lista das com idade acima da média nome: {lista_pessoas_sup_media}.')
print('*'*50)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 094: Crie um programa que leia nome, 
sexo e idade de várias pessoas, guardando os dados de 
cada pessoa em um dicionário e todos os dicionários em 
uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""