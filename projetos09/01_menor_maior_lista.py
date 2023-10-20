mensagem = 'MENOR-MAIOR LISTA'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

contador = 0
lista_valor = []

while contador < 5:
    valor_informado = int(input(f'Digite o {contador +1 }º valor: '))
    lista_valor.append(valor_informado)
    contador += 1
print('*'*50)

print(f'O menor valor da lista é: {min(lista_valor)} e o maior {max(lista_valor)}.')




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 078: Faça um programa que leia 5 valores 
numéricos e guarde-os em uma lista. No final, mostre qual 
foi o maior e o menor valor digitado e as suas respectivas 
posições na lista.
"""