mensagem = 'LISTA ORDENADA SEM Sort'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

contador = 0
lista_valor = []


while contador < 5:
    valor_informado = int(input(f'Digite o {contador + 1}º valor: '))
    if contador == 0 or lista_valor[-1] < valor_informado:
        lista_valor.append(valor_informado)
        print(f'O valor {valor_informado} foi adicionado no final da lista com sucesso.')
    else: 
        j = 0  
        while j < len(lista_valor):
            if lista_valor[j] > valor_informado:
                lista_valor.insert(j, valor_informado)
                print(f'O valor {valor_informado} foi adicionado na {j}º posição com sucesso.')
                break
            j += 1
    contador += 1

print('*'*50)

print('Os valores da lista são: ', end='')
for element in lista_valor:
    print(element, end=' ')






# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 080: Crie um programa onde o usuário possa digitar 
cinco valores numéricos e cadastre-os em uma lista, já na posição 
correta de inserção (sem usar o sort()). No final, mostre a lista 
ordenada na tela.
"""