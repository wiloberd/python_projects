from random import shuffle

mensagem = 'APRESENTAÇÃO SEQUENCIA'
print('*'*55)
print('{:^55}'.format(mensagem))
print('*'*55)

nome_primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
nome_secundo_aluno = str(input('Digite o nome do primeiro aluno: '))
nome_terceiro_aluno = str(input('Digite o nome do primeiro aluno: '))
nome_quarto_aluno = str(input('Digite o nome do primeiro aluno: '))

nome_alunos = [nome_primeiro_aluno, nome_secundo_aluno, nome_terceiro_aluno, nome_quarto_aluno]

shuffle(nome_alunos)

print('A ordem de apresentação será da forma seguinte: ')
print(nome_alunos)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 20: O mesmo professor do desafio 19 quer 
sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e 
mostre a ordem sorteada.

"""