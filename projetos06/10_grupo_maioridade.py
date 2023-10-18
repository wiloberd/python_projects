from datetime import date

mensagem = 'GRUPO MAIORIDADE'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

maior = 0
menor = 0

for posicao in range(0, 7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {posicao + 1}º pessoa: '))
    idade =  date.today().year - ano_nascimento
    if (idade >= 21):        
        maior = maior + 1
    else:
        menor = menor + 1

print(f'Ao todo { maior } pessoa(s) já são maiores e {menor} pessoa(s) não atingiram a maioridade.')

print('*'*40)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 54: Crie um programa que leia o ano 
de nascimento de sete pessoas. No final, mostre quantas 
pessoas ainda não atingiram a maioridade e quantas 
já são maiores.
"""
