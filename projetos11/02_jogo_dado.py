from random import randint
from operator import itemgetter

mensagem = 'JOGO DADO'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


dict_jogador = {}


for jogador in range(0, 4):
    dict_jogador[jogador + 1] = randint(0, 6)

for key, jogo in dict_jogador.items():
    print(f'O jogoador {key} --> tirou: {jogo} no dado.' )




lista_values = []
dict_jogador_ordenada = {}

# acicionando os valores sorteado por cada jogador em uma nova lista
for value in dict_jogador.values():
    lista_values.append(value)

# ordenando a lista dos valores sorteado por cada jogador decrescentemente
lista_values.sort(reverse=True)


# analizando cada valor jogado para identificar o ranking de cada jogador
print('*'*50)

for index, element in enumerate(lista_values):
    for key, value in dict_jogador.items():
        if element == value:
            dict_jogador_ordenada[index] = key
            dict_jogador[key] = 'null'
            break

# imprimindo o ranking dos ganhadores
for key, value in dict_jogador_ordenada.items():
    print(f'{key+1}º Lugar jogador {value} com {lista_values[key]}' )

print('*'*50)
