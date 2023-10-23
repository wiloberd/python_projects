mensagem = 'CADASTRO JOGADOR'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)




dicionario_jogodar = {}
lista_gol = []

# lendo os valores do jogador
nome_informado = str(input('Informe o nome completo do jogador: '))
quantidade_partida = int(input('Quantidade de partidadas: '))

# adicionando os valores do jogador no dicionario
dicionario_jogodar['nome'] = nome_informado
dicionario_jogodar['partida'] = quantidade_partida

# lendo e adicionando a quantidade de gol por jogo em uma lista
for index in range(0, quantidade_partida):
    gol = int(input(f'Informe a quantidade de gol na {index + 1}º partida: '))
    lista_gol.append(gol)

# adicionando a lista de gol por jogo do jogador no dicionario
dicionario_jogodar['gol_partida'] = lista_gol



print('*'*50)
# calculando o aproveitamento total
total_gol = sum(lista_gol)
dicionario_jogodar['aroveitamento'] = total_gol

# saida do programa
for key, value in dicionario_jogodar.items():
    print(f'{key}: {value}')

print('*'*50)

print(f'O {nome_informado} jogou {quantidade_partida} partidadas.')

if len(dicionario_jogodar.items()) != 0:
    if len(dicionario_jogodar['gol_partida'] ) > 0:
        for index, gol in enumerate((dicionario_jogodar['gol_partida'] )):
            print(f'--> Na {index + 1}º partida fez {gol} gols.')
    else:
        pass

print('*'*50)




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de 
um jogador de futebol. O programa vai ler o nome do jogador e quantas 
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols 
feitos durante o campeonato.
"""