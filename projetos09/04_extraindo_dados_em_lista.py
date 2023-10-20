mensagem = 'LISTA ORDENADA SEM Sort'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

contador_numero = 0
lista_valor = []
resposta = 'S'


while resposta == 'S':
    valor_informado = int(input(f'Digite o valor a ser inserido na lista: '))
    lista_valor.append(valor_informado)
    contador_numero += 1
    resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Informe uma resposta valida...')
        resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]

    if resposta == 'N':
        break

print('*'*50)
# mostrando os valores
print(f'Ao todo foi digitado {contador_numero} numero..')
print(f'A lista decrescente ficou: ', end= '')

lista_valor.sort(reverse=True)

for element in lista_valor:
    print(element, end=' ')

print('| FIM')

if 5 in lista_valor:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')

print('*'*50)





# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 081: Crie um programa que vai ler vários números 
e colocar em uma lista. Depois disso, mostre:             

A) Quantos números foram digitados.                              
B) A lista de valores, ordenada de forma decrescente. 
C) Se o valor 5 foi digitado e está ou não na lista.
"""