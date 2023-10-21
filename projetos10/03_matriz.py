mensagem = 'MATRIZ 3X3'
mensagem_alternativa = 'MATRIZ RESULTANTE'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


matriz = [[], [], []]


for i in range(0, 3):
    
    for j in range(0, 3):
        valor_informado = int(input('Informe um valor: '))

        if i == 0:
            matriz[i].append(valor_informado)
        elif i == 1:
            matriz[i].append(valor_informado)
        elif i == 2:
            matriz[i].append(valor_informado)


print('*'*50)
print('{:^50}'.format(mensagem_alternativa))
print('*'*50)

for i in range(0, 3):
    for j in range(0, 3):
        if i == 0:
            print(matriz[i][j], end='| ')
        elif i == 1:
            print(matriz[i][j], end='| ')
        elif i == 2:
            print(matriz[i][j], end='| ')
    print()
print('*'*50)

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 086: Crie um programa que declare uma 
matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
"""