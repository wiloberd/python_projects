mensagem = 'SITUAÇÃO ALUNO'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

dict_aluno = {}
situcao_aprovado = 'APROVADO'
situcao_recuperacao = 'RECUPERÇÃO'
situcao_reprovado = 'REPROVADO'

nome_informado = str(input('Informe o nome do aluno: '))
media_informado = float(input(f'Informe a média do {nome_informado}: '))

if media_informado >= 7:
    dict_aluno['nome'] = nome_informado
    dict_aluno['media'] = media_informado
    dict_aluno['situcao'] = situcao_aprovado

elif media_informado <= 5:
    dict_aluno['nome'] = nome_informado
    dict_aluno['media'] = media_informado
    dict_aluno['situcao'] = situcao_recuperacao

if media_informado < 7 and media_informado >= 5:
    dict_aluno['nome'] = nome_informado
    dict_aluno['media'] = media_informado
    dict_aluno['situcao'] = situcao_reprovado

print('*'*50)


for key, value in dict_aluno.items():
    print(f'{key}: {value}')
print('*'*50)