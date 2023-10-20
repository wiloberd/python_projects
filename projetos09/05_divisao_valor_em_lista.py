mensagem = 'PAR/IMPAR em LISTA'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

lista_valor = []
lista_par = []
lista_impar = []
resposta = 'S'


while resposta == 'S':
    valor_informado = int(input(f'Digite o valor a ser inserido na lista: '))
    lista_valor.append(valor_informado)
    
    resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Informe uma resposta valida...')
        resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]

    if resposta == 'N':
        break

for element in lista_valor:
    if (element % 2) == 0:
        lista_par.append(element)
    elif(element % 2 ) != 0:
        lista_impar.append(element)

print('*'*50)



# mostrando os valores da primeira lista
print(f'A lista ficou: ', end= '')

for element in lista_valor:
    print(element, end=' ')

print('| FIM')


# mostrando os valores da primeira lista
print('A lista dos pares ficou: ', end= '')

for element in lista_par:
    print(element, end=' ')

print('| FIM')


# mostrando os valores da primeira lista
print('A lista dos impares ficou: ', end= '')

for element in lista_impar:
    print(element, end=' ')

print('| FIM')

# separador horizontal no final
print('*'*50)




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 082: Crie um programa que vai ler vários 
números e colocar em uma lista. Depois disso, crie duas 
listas extras que vão conter apenas os valores pares e 
os valores ímpares digitados, respectivamente. Ao final, 
mostre o conteúdo das três listas geradas.
"""