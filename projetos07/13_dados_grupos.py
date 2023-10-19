mensagem = 'DADOS GRUPOS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

pessoas_maior_idade = 0
quantidade_homem = 0
quantidade_mulheres = 0
grupo_mulheres_menor = 0
resposta = 'S'

while resposta == 'S':
    idade_informada = int(input(f'Informe a idade da pessoa: '))
    sexo_informada = str(input(f'Informe o sexo da pessoa: ')).upper().strip()
    print('*'*40)

    if idade_informada > 18:
        pessoas_maior_idade =+ 1
    
    # verificação homemens         
    if sexo_informada == 'M':
        quantidade_homem += 1

    # verificação mulheres         
    if sexo_informada == 'F':
        if idade_informada < 20:
            grupo_mulheres_menor =+ 1
                
    resposta = str(input('Deseja cadastrar mais pessoas (S/N): ')).upper().strip()[0]
    if resposta == 'N':
        break
    else:
        print('*'*40)

print('*'*40)

print('A quantidade de pessoas com mais de 18 anos é {}.'.format(pessoas_maior_idade))
print('A quantidade de homem cadastrados foi {}.'.format(quantidade_homem))
print(f'Tem {grupo_mulheres_menor} mulher com menos de 20 anos, e um total {quantidade_mulheres} mulheres cadastrado.')
print('*'*40)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 69: Crie um programa que leia a idade 
e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""