
mensagem = 'MAIOR PESO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

maior = 0
menor = 0
peso_informado = 0

for posicao in range(1, 6):
    peso_informado = float(input(f'Digite o peso da {posicao}º pessoa: '))
    if posicao == 1:
        # Para evitar que o valor 0 seja considerada na primeira iteração
        if peso_informado != 0:
            maior = peso_informado
            menor = peso_informado
        else:
            while peso_informado == 0:
                peso_informado = float(input(f'Digite o peso da {posicao}º pessoa: '))
            maior = peso_informado
            menor = peso_informado
            continue
    else:
        if (peso_informado > maior):        
            maior = peso_informado
        if (peso_informado < menor):
            menor = peso_informado
    
print(f'Ao todo o maior peso informado foi { maior } Kg e o menor peso foi {menor} Kg.' if maior != menor else 'Pesos informados são iguais!')

print('*'*40)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 55: Faça um programa que leia o peso 
de cinco pessoas. No final, mostre qual foi o maior 
e o menor peso lidos.
"""