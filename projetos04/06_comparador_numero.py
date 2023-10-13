mensagem = 'COMPARADOR DE NUMERO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

primeiro_numero = int(input('Informe o primeiro numero: '))
segundo_numero  = int(input('Informe o secundo numero: '))
terceiro_numero  = int(input('Informe o terceiro numero: '))

menor_numero = primeiro_numero
maior_numero = primeiro_numero

# comparador do menor numero
if (segundo_numero < primeiro_numero and segundo_numero < terceiro_numero):
    menor_numero = segundo_numero
if (terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero):
    menor_numero = terceiro_numero

# comparador do maior numero
if (segundo_numero > primeiro_numero and segundo_numero > terceiro_numero):
    maior_numero = segundo_numero
if (terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero):
    maior_numero = terceiro_numero


print(f'O maior numero é: {maior_numero}')
print(f'O menor numero é: {menor_numero}')
# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 33: Faça um programa que leia três números 
e mostre qual é o maior e qual é o menor.
"""