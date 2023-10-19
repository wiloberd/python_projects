mensagem = 'SEXO DO USUARIO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)



sexo_informado = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo_informado != 'M' and sexo_informado != 'F':
    print('Sexo informado Invalido, deve ser (M) ou (F)')
    sexo_informado = str(input('Informe seu sexo: ')).strip().upper()[0]

print(f'O sexo {sexo_informado} foi registrado com sucesso.')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 57: Faça um programa que leia o sexo de 
uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até 
ter um valor correto.
"""