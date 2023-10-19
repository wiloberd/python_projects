mensagem = 'DADOS GRUPOS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

total_gasto = 0
quantidade_produto_maior_mil = 0
preco_produto_mais_barato = 0
contador = 1
nome_produto_barato = ''
resposta = 'S'


while resposta == 'S':
    nome_produto = str(input(f'Informe o nome do produto: '))
    preco_produto = float(input(f'Informe o preco do produto: '))
    total_gasto = total_gasto + preco_produto
    print('*'*40)

    # quantidade produto maior que 1000 
    if preco_produto > 1000:
        quantidade_produto_maior_mil += 1
    
    # produto mais barato        
    if contador == 1:
        preco_produto_mais_barato = preco_produto
        contador += 1
    else:
        if preco_produto_mais_barato > preco_produto:
           preco_produto_mais_barato = preco_produto
           nome_produto_barato = nome_produto
                
    resposta = str(input('Deseja cadastrar mais produtos (S/N): ')).upper().strip()[0]
    if resposta == 'N':
        break
    else:
        print('*'*40)

print('*'*40)

print('O total gasto na compra foi R${:.2f}.'.format(total_gasto))
print('A quantidade de produto que custou mais de R$1000 foi {}.'.format(quantidade_produto_maior_mil))
print('O nome do produto mais barato é ** {} **., e custou R${}'.format(nome_produto_barato.upper(), preco_produto_mais_barato ))
print('*'*40)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 70: Crie um programa que leia o nome 
e o preço de vários produtos. O programa deverá perguntar 
se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""