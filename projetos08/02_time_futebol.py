mensagem = 'TIME FUTEBOL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)


teams_brasileiro = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Flamengo', 'internacional', 'Bragantino', 'São Paulo', 'Santo', 'Botafogo', 'Ceará SC', 'Goiáis', 'Avaí', 'Cuibá', 'Chapecoense', 'Coritiba', 'Améria-MG', 'Atlético-GO', 'Fortaleza', 'Juventude')




print('Os 5 primeiros times colocados são: {}.'.format( teams_brasileiro[0:5]))
print('*'*40)


print('Os 4 ultimos colocados são: {}.'.format(teams_brasileiro[-4:]))
print('*'*40)

print('Os times em ordem alfabéticos: \n{}'.format(sorted(teams_brasileiro)))
print('*'*40)

print('O times Chapecoense está na {}º posição.'.format(teams_brasileiro.index('Chapecoense')))
print('*'*40)




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 73: Crie uma tupla preenchida com os 
20 primeiros colocados da Tabela do Campeonato Brasileiro 
de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""