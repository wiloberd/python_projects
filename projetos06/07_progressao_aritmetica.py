mensagem = 'PROGRESSÃO ARITMETICA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)


primeiro_termo = int(input('Informe o primeiro termo: '))
pa = int(input('Informe a progressão aritmetica: '))
ultimo_termo = primeiro_termo * pa

for posicao in range( primeiro_termo, ultimo_termo):
    
    print('{}º termo é {}.'.format(posicao))



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 51: Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.
"""