mensagem = 'FATORIAL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

numero_informado = int(input('Informe o numero: '))
var = numero_informado
fatorial = 1

while var > 0:
    fatorial = fatorial * var
    print('{}'.format(var), end= '')
    print(' x ' if var > 1 else ' = ', end= '' )
    var = var - 1

print(fatorial)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 060: Faça um programa que leia um número qualquer 
e mostre o seu fatorial. Exemplo:
"""