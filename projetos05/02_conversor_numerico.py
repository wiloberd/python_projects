mensagem = 'CONVERSOR DE BASE NUMERICO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

valor_informado = int(input('Informe o valor a ser convertido: '))
opcao = 1

print('Informe a base, escolhendo uma das opções abaixo..')

print('[1] Base BINÁRIO ')
print('[2] Base OCTAL ')
print('[3] Base HEXADECIMAL ')

base_informado = int(input('Digite a opão escolhida: '))

if (base_informado == 1):
    print('O valor binário de {} é {}'.format(valor_informado, bin(valor_informado)[2:]))
elif (base_informado == 2):
    print('O valor octal de {} é {}'.format(valor_informado, oct(valor_informado)[2:]))
elif (base_informado == 3):
    print('O valor hexadecimal de {} é {}'.format(valor_informado, hex(valor_informado)[2:]))
else:
    print("Opção invalida!")

# SOBRE O EXERCICIO PROPOSTO

"""
Exercício Python 37: Escreva um programa em Python que 
leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 
1 para binário, 
2 para octal e 
3 para hexadecimal.
"""