mensagem = 'MENOR-MAIOR LISTA'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

contador = 0
lista_valor = []


while contador < 5:
    valor_informado = int(input(f'Digite o {contador + 1}º valor: '))
    contador += 1
    if valor_informado not in lista_valor:
        lista_valor.append(valor_informado)
        print('Valor adicionado com sucesso.')
    else:
        pass

print('*'*50)

lista_valor.sort()
print('Os valores da lista são: ', end='')
for element in lista_valor:
    print(element, end=' ')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 079: Crie um programa onde o usuário possa digitar 
vários valores numéricos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. No final, serão exibidos 
todos os valores únicos digitados, em ordem crescente.
"""