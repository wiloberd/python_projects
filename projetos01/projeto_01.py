numero1 = input('Numero 1: ')
numero2 = input('Numero 2: ')

soma = int(numero1)+int(numero2)

# diferente forma de usar a função print
print('A soma vale:', soma)
print(f'A soma vale: {soma}')
print('A soma vale: {}'.format(soma))
# propositalmente defini a ordem das variveis nas placeholders equivocadamente
print('A soma entre {0} e {2} vale: {1}'.format(numero1, numero2, soma))

# função buit-in para verificação de tipos
print(f'É um numero: {numero1.isnumeric()}')
print(f'É um caracter: {numero1.isalpha()}')
print(f'É alfanumerico: {numero1.isalnum()}')