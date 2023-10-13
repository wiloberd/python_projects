import random

mensagem = 'RANDOM PUPIL'
print('*'*55)
print('{:^55}'.format(mensagem))
print('*'*55)

nome_alunos = ['Fernando', 'Joe', 'Samuel', 'Peter']

aluno_selecionado = random.choice(nome_alunos)

print('Por sorte, o aluno escolhido foi {:*^10}'.format(aluno_selecionado))

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 19: Um professor quer sortear um dos 
seus quatro alunos para apagar o quadro. Faça um programa 
que ajude ele, lendo o nome dos alunos e escrevendo na 
tela o nome do escolhido.

"""