# Exercício Python 14: Escreva um programa que converta uma 
# temperatura digitando em graus Celsius e converta para graus Fahrenheit.

mensagem = 'CONVERTISSOR DE TEMPERATURA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

grau_celcius = float(input('Digite o temperatura a ser convertido: '))

# calculando a temperaturo de celcius para Fahreinheit.
grau_fahrenheit = ((grau_celcius * 9) / 5) + 32

print('A conversão de {}ºC para Fahreinheit é igual a: {}ºF!'.format(grau_celcius, grau_fahrenheit))