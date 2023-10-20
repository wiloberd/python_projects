mensagem = 'CONTADOR VOGAIS'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)


teams_brasileiro = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Flamengo')



for element in teams_brasileiro:
    print('A palavra \033[0;32m{}\033[m tem como vogal: '.format(element.upper()), end= '')
    for letra in element:
        if letra in 'aeiouyAEIOUY':
            print(letra, end= ' ')
    print('')

print('*'*50)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 077: Crie um programa que tenha uma tupla com 
várias palavras (não usar acentos). Depois disso, você deve mostrar, 
para cada palavra, quais são as suas vogais.
"""