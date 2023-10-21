from time import sleep

mensagem = 'BOLETIM DE ALUNO'
mensagem_cabecalho = 'NOME ALUNO | MEDIA'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

lista_alunos = []
aluno = []
media_aluno = []

resposta = 'S'


while resposta == 'S':
    nome_informado = str(input(f'Digite o nome completo da pessoa: '))
    primeira_nota = float(input(f'Digite a primeira nota do aluno: '))
    segunda_nota = float(input(f'Digite a segunda nota do aluno: '))


    # inserindo cada grupo de dados de cada aluno na lista de alunos
    aluno.append(nome_informado)
    aluno.append(primeira_nota)
    aluno.append(segunda_nota)
    lista_alunos.append(aluno[:])
    aluno.clear()

    resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]
    while resposta != 'N' and resposta != 'S':
        print('Informe uma resposta valida...')
        resposta = str(input('Deseja adicionar um outro valor na lista (S/N): ')).upper().strip()[0]

    if resposta == 'N':
        break



for aluno in lista_alunos:
    # calcular media de cada aluno
    media = ( aluno[1] + aluno[2] ) / 2

    # associando cada aluno e sua media em uma sublista
    sub_media = []
    sub_media.append(aluno[0])
    sub_media.append(media)

    # adicionando os valores na coleção de media por alunos
    media_aluno.append(sub_media[:])
    sub_media.clear()

print('*'*50)
print('Loading...')
sleep(2)

# impressão final dos dados
print('*'*30)
print('{:^30}'.format(mensagem))
print('{:^30}'.format(mensagem_cabecalho))
print('*'*30)

nome_informado.capitalize
for aluno in media_aluno:
    nome = str(aluno[0])
    print('{:<20}: {:.1f}'.format(nome.title(), aluno[1]))

print('*'*30)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 089: Crie um programa que leia nome e duas notas 
de vários alunos e guarde tudo em uma lista composta. No final, 
mostre um boletim contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente.
"""