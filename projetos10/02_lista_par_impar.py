mensagem = 'LISTA UNICA PAR/IMPAR'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


contador = 0
lista_valores = [[],[]]


while contador < 7:
    valor_informado = int(input('Informe um valor: '))
    contador += 1

    if valor_informado % 2 == 0:
        lista_valores[0].append(valor_informado)
    elif valor_informado % 2 != 0:
        lista_valores[1].append(valor_informado)


# adicionando separadamente os valores impar e par na lista dos valores
lista_valores[0].sort()
lista_valores[1].sort()


# impressão final da lista dos valores
print('*'*50)
print('Com os valores ordenada e agrupada em par e impar a lista ficou:', lista_valores)
print('*'*50)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 085: Crie um programa onde o usuário possa 
digitar sete valores numéricos e cadastre-os em uma lista única 
que mantenha separados os valores pares e ímpares. No final, 
mostre os valores pares e ímpares em ordem crescente.
"""