from datetime import date

mensagem = 'ALISTAMENTO MILITAR'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

ano_nascimento = int(input('Informe a idade do cadidato: '))

idade_cadidato = date.today().year - ano_nascimento

if (idade_cadidato < 18 ):
    tempo_faltante = 18 -  idade_cadidato
    ano_ideal = date.today().year + tempo_faltante
    print('Vair ter que esperar {} anos para se alistar.'.format(tempo_faltante))
    print('Você poderá se alistar a partir do ano {}.'.format(ano_ideal))
elif (idade_cadidato >= 18 and idade_cadidato <= 18):
    tempo_faltante = 18 -  idade_cadidato
    print('É a hora de se alistar, porém tem até {} anos para fazer isso.'.format(tempo_faltante))
elif ( idade_cadidato > 18):
    tempo_exendente = idade_cadidato - 18
    ano_ideal = date.today().year -tempo_exendente
    print('Tem {} anos a mais da idade limita, não pode mais se alistar para o exercito.'.format(tempo_exendente))
    print('Você deveria ter se alistado desdo o ano {}.'.format(ano_ideal))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 39: Faça um programa que leia o ano de nascimento 
de um jovem e informe, de acordo com a sua idade, se ele ainda vai 
se alistar ao serviço militar, se é a hora exata de se alistar ou 
se já passou do tempo do alistamento. Seu programa também deverá 
mostrar o tempo que falta ou que passou do prazo.
"""