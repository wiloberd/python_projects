from datetime import date

mensagem = 'CADASTRO TRABALHADOR'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


idade_pessoa = 0
ano_aposentado = 0
tempo_funcao = 35
dicionario_trabalhadores = {}

nome_informado = str(input('Informe o nome completo da pessoa: '))
ano_nascimento_informado = int(input('Informe o ano de nascimento: '))


# calculando a idade 
idade_pessoa = date.today().year - ano_nascimento_informado


dicionario_trabalhadores['nome'] = nome_informado
dicionario_trabalhadores['nascimento'] = ano_nascimento_informado
dicionario_trabalhadores['idade'] = int(idade_pessoa)


ctps_informado = str(input('Informe o numero da carteira de trabalho ou o numero zero (0) se não tiver: '))

if ctps_informado != '0':
    ano_contratacao = int(input('Informe o ano inicial do contrato: '))
    salario_funcionario = float(input('Informe o seu salario: '))
    dicionario_trabalhadores['salario'] = salario_funcionario


    dicionario_trabalhadores['ctps'] = ctps_informado
    dicionario_trabalhadores['ano_contratacao'] = ano_contratacao

    # calclar ano aposentadoria
    ano_aposentado = ( ano_contratacao - ano_nascimento_informado ) + tempo_funcao
    dicionario_trabalhadores['aposentadoria'] = ano_aposentado
else:
    pass

print('*'*50)
for key, value in dicionario_trabalhadores.items():
    print(f'{key}: {value}')
print('*'*50)

