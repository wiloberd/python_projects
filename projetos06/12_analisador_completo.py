from datetime import date


mensagem = 'ANALISADOR COMPLETO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

idade_homem_maior = 0
nomme_velho_homem = ''
grupo_mulheres_menor = 0
soma_idade = 0
media_idade = 0

quantidade_pessoas = 2

for posicao in range(0, quantidade_pessoas):
    for n in range(0, 1):
        nome_completo    = str(input(f'Informe o nome completo da {posicao + 1}º pessoa: '))
        idade_informada = int(input(f'Informe a idade da  {posicao + 1}º pessoa: '))
        sexo_informada = str(input(f'Informe o sexo da {posicao + 1}º pessoa: ')).upper().strip()

        # verificação homemens         
        if sexo_informada == 'M':
            if idade_informada > idade_homem_maior:
                idade_maior = idade_informada
                nomme_velho_homem = nome_completo

        # verificação mulheres         
        if sexo_informada == 'F':
            if idade_informada < 20:
                grupo_mulheres_menor += 1
                
            
    soma_idade = soma_idade + idade_informada
    media_idade = soma_idade / quantidade_pessoas

print('*'*40)

print('A média das idades é {:.1f}'.format(media_idade))
print(f'O nome do homem mais velho é: {nomme_velho_homem.upper()}' if nomme_velho_homem != '' else 'Não foi informado nenhuma pessoa de sexo masculino.')
print(f'Tem {grupo_mulheres_menor} mulher com menos de 20 anos.' if grupo_mulheres_menor == 1 else f'São {grupo_mulheres_menor} mulheres menos de 20 anos.')

print('*'*40)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 56: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho 
e quantas mulheres têm menos de 20 anos.
"""