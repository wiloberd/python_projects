mensagem = 'APROVEITAMENTO JOGADOR V2.0'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


dicionario_jogodar = {}
lista_jogador = []
lista_gol = []
total_gol_jogador = []
resposta = 'S'

while resposta == 'S':

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
    dicionario_jogodar['gol_partida'] = lista_gol[:]

    # adicionando informações de cada jogador em uma coleção de lista
    lista_jogador.append(dicionario_jogodar.copy())
    lista_gol.clear()
    print('*'*50)


    resposta = str(input('Deseja adicionar mais pessoas na lista (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Informe uma resposta valida...')
        resposta = str(input('Deseja adicionar mais pessoas na lista (S/N): ')).upper().strip()[0]

    if resposta == 'N':
        break


print('*'*50)

# inserindo  o aproveitamento total de cada jogador em uma lista
for jogador in lista_jogador:
    total_gol_jogador.append(sum(jogador['gol_partida']))
    


# a formatação da saida precisa ser refinado.
# listando estatistica dos jogadores
print('Cod     Nome              gols           total')
for index, jogador in enumerate(lista_jogador):
    print('{}       {}           {}           {}'.format(index, jogador['nome'], jogador['gol_partida'], total_gol_jogador[index]))
    pass 
    
print('*'*50)



# levantamento detalhada de cada jogador.
levantamento_resposta = 'S'

while levantamento_resposta == "S":
    levantamento_resposta = str(input('Gostaria de ver um levantamento detalhada de um jogador? (S/N): ')).upper().strip()[0]

    if levantamento_resposta != 'N' and levantamento_resposta != 'S':
        print('Resposta invalida! por favor responda (S/N)')
        levantamento_resposta = str(input('Gostaria de ver um levantamento detalhada de um jogador? (S/N): ')).upper().strip()[0]

    elif levantamento_resposta == 'N':
        break
    else:
        while True:
            codigo_jogador = int(input('Informe o codigo do jogador desejada :--> ou 999 para  SAIR <--: '))

            if codigo_jogador == 999:
                levantamento_resposta = 'N'
                break
            elif codigo_jogador < 0 or codigo_jogador > len(lista_jogador):
                print('Codigo do jogador não encontrado, use um dos codigos listado.')
            else:
                print('*'*50)
                print('LEVANTAMENTO DO JOGADOR {}'.format(lista_jogador[codigo_jogador]['nome']))
                print('*'*50)

                for index, value in enumerate(lista_jogador[codigo_jogador]['gol_partida']):
                    print('No {}º jogo fez {}'.format((index + 1), value))
                print('*'*50)


print('*'*50)
print('FIM DO PROGRAMA')
print('*'*50)




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione 
com vários jogadores, incluindo um sistema de visualização de detalhes 
do aproveitamento de cada jogador.
"""