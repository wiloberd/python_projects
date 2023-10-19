
mensagem = 'MAIOR PESO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

maior = 0
menor = 0
media_aritmetica = 0
quantidade_numero = 0
resposta = 'S'

while resposta != 'N':
    quantidade_numero += 1
    numero_informado = float(input(f'Digite o {quantidade_numero}º numero: '))
    resposta = str(input('Gostaria de informar mais valores S/N: ')).upper().strip()[0]
    if quantidade_numero == 1:
        # Para evitar que o valor 0 seja considerada na primeira iteração
        if numero_informado != 0:
            maior = numero_informado
            menor = numero_informado
        else:
            while numero_informado == 0:
                quantidade_numero += 1
                numero_informado = float(input(f'Digite o {quantidade_numero}º numero: '))
                resposta = str(input('Gostaria de informar mais valores S/N: ')).upper().strip()[0]
            maior = numero_informado
            menor = numero_informado
            continue
    else:
        if (numero_informado > maior):        
            maior = numero_informado
        if (numero_informado < menor):
            menor = numero_informado
    
print(f'Ao todo o maior valor lido foi { maior } e o menor valor foi {menor}.' if maior != menor else 'Valores informados são iguais! e foi {:.0f}'.format(numero_informado))

print('*'*40)



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 65: Crie um programa que leia vários números 
inteiros pelo teclado. No final da execução, mostre a média entre 
todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar 
a digitar valores.
"""