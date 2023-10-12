# Programa que calcular novo preço com 5% de desconto.

preco_produto = float(input('Digite o preço do produto: '))

# definindo um desconto de 5%
valor_desconto = 5
# calculando o desconto de 5%
desconto = (preco_produto * valor_desconto ) / 100

# aplicando o desconto de 5%
novo_preco_produto = preco_produto - desconto

print('O novo preço do produto é do produto será {:.2f}'.format(novo_preco_produto))