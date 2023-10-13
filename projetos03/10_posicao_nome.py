
nome_usuario = str(input('Informe o nome completo do usuario: '))

nome_dividido = nome_usuario.strip().split()

print('O nome informado: ', nome_usuario)
print('O seu primeiro nome: {}'.format(nome_dividido[0]))
print('O seu último nome: {}'.format(nome_dividido[-1]))

# outra forma de determinar a último elemento em lista
print('O seu último nome: {}'.format(nome_dividido[len(nome_dividido) - 1]))



"""
Exercício Python 27: Faça um programa que leia o nome 
completo de uma pessoa, mostrando em seguida o primeiro 
e o último nome separadamente.
"""