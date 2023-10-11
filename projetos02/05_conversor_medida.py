# Este programa leia um valor em metro(m) (aceita valor decimal) 
# e converte ele em milimetro (mm) e centimetros (cm)

mensagem = 'CONVERTISSOR DE MEDIDAS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

valor = float(input('Digite o valor a ser convertido: '))
resultado_centimetro = valor * 100
resultado_milimetro =  valor * 1000

print('A conversão de {} metro para centimetro, é igual a {} CM.'.format(valor, resultado_centimetro))
print('A conversão de {} metro para milimetro, é igual a {} MM.'.format(valor, resultado_milimetro))
