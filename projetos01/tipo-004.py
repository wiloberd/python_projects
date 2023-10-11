"""
Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e alguns informações (propriedades)
sobre ela """

user_input = input('Digite alguma coisa: ')

print(f'É um inteiro: {user_input.isnumeric()}')
print(f'É um caractere: {user_input.isalpha()}')
print(f'Esta em maiúculo: {user_input.isupper()}')
print(f'Esta capitalizado: {user_input.istitle()}')
print(f'É alfanumérico: {user_input.isalnum()}')