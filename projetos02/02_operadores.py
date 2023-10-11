# ordem de precedência de calculos
# // Divisão inteira
# %  Resto da divisão

# ()
# ** potencia
# * 
# * / // %
# + - 

print('''Este programa calcula e mostra 
o resuldado de dois numeros nas operações 
aritmeticas basicas.
''')

first_number = int(input('Digite o primeiro numero: '))
seconde_number = int(input('Digite o secundo numero: '))

soma =  first_number + seconde_number
divisao = first_number / seconde_number
divisao_inteira = first_number // seconde_number
resto_divisao = first_number % seconde_number
potencia = first_number ** seconde_number

# considerando o primeiro numero digitado pelo usuario
raiz_quadrada = first_number ** (1/2)

mensagem_principal = 'RESULTADO'
outra_mensagem = 'SEGUNDA PARTE'
# imprimindo os resultado
print('*'*35)
print('{:^35}'.format(mensagem_principal))
print('*'*35)
print('''A soma é {}, a divisão é {}, 
a potencia é {}, a raiz quadrada 
do primeiro numero é {}.'''.format(soma, divisao, potencia, raiz_quadrada))

print('*'*35)
print('{:^35}'.format(outra_mensagem))
print('*'*35)
print(' A parte inteira da divisão \n do primeiro numero é {}, o resto é {}'.format(divisao_inteira, resto_divisao))