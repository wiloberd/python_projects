from datetime import date

mensagem = 'CLASSIFICADOR DE ATLETAS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

ano_nascimento = int(input('Informe a idade do atleta: '))

idade_atleta = date.today().year - ano_nascimento


if (idade_atleta <= 9):
    print('Tendo {} anos, o atleta está na categoria MIMIM'.format(idade_atleta))
elif(idade_atleta <= 14):
    print('Tendo {} anos, o atleta está na categoria INFANTIL'.format(idade_atleta))
elif(idade_atleta <= 19):
    print('Tendo {} anos, o atleta está na categoria JÚNIOR'.format(idade_atleta))
elif(idade_atleta <= 25):
    print('Tendo {} anos, o atleta está na categoria SÊNIOR'.format(idade_atleta))
else:
    print('Tendo {} anos, o atleta está na categoria MASTER'.format(idade_atleta))




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 041: A Confederação Nacional de Natação 
precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""