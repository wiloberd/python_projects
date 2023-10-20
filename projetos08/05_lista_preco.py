
mensagem = 'LISTA DE PRECO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

produtos = ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)


for index, item in enumerate(produtos):
    if index % 2 == 0:
        print('{:.<30}'.format(item), end='')
    elif index % 2 != 0:
        print('R$ {:>7.2f}'.format(item))

print('*'*40)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 076: Crie um programa que tenha uma tupla única 
com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados 
em forma tabular.
"""