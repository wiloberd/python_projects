# Este programa calcula quantos dolar uma pessoa pode 
# comprar considerando o saldo na sua carteira ou 
# no seu cartão de debito.

mensagem = 'CONVERTISSOR MOEDAS BRL-USD'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

# cotação do dollar hoje : 5.06 
cotacao = 5.06

saldo = float(input('Informe a quantidade de dinheiro a ser convertido: '))

exchange = saldo / cotacao

print('R$ {:.2f} BRL vale $ {:.2f} USD'.format(saldo, exchange))