mensagem = 'MATRIZ 3X3'
mensagem_alternativa = 'MATRIZ RESULTANTE'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


matriz = [[], [], []]
soma_valores = 0
soma_valores_terceira = 0
soma_valores_segunda = 0


for i in range(0, 3):
    
    for j in range(0, 3):
        valor_informado = int(input('Informe um valor: '))
        soma_valores = soma_valores + valor_informado
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
            soma_valores_segunda = soma_valores_segunda + valor_informado
        elif i == 2:
            print(matriz[i][j], end='| ')
            
    print()

for i in range(0, 3):
    soma_valores_terceira = soma_valores_terceira + matriz[i][2]


print('*'*50)
print('A soma de todos os valores digitado é: ', soma_valores )
print('A soma de todos os valores da terçeira coluna é:',soma_valores_terceira)
print('O maior valor da segunda linha é: ',max(matriz[1]))

print('*'*50)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 087: Aprimore o desafio anterior, 
mostrando no final:   

A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
"""