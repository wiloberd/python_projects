mensagem = 'COMPARADOR DE NUMERO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

primeiro_numero = float(input('Informe o primeiro numero: '))
segungo_numero = float(input('Informe o segundo numero: '))

if(primeiro_numero > segungo_numero):
    print(f'O primeiro numero é o maior: {primeiro_numero}')
elif(segungo_numero > primeiro_numero):
    print(f'O segundo numero é o maior: {segungo_numero}')
else:
    print(f'Não exite numero maior.')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 038: Escreva um programa que leia dois números 
inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""