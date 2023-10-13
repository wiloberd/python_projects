nome_completo = str(input('Informe seu nome completo: '))

print('Seu nome em majuscula: ', nome_completo.upper())
print('Seu nome em minuscula:', nome_completo.lower())

# removendo os espeços execivos digitado pelo usuario.
nome_tratado = nome_completo.strip()

# dividir cada parte do nome numa lista de string
nome_dividido = nome_completo.split()

# removendo os espaços
len_nome_completo = len(nome_tratado) - nome_tratado.count(' ')

print('Seu nome completo tem {} letras'.format(len_nome_completo) )
print(f'O seu primeiro nome tem {len(nome_dividido[0])} letras')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 22: Crie um programa que leia o nome 
completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

"""