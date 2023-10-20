mensagem = 'NUMERO POR EXTENSO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

numero_informado = int(input('Digite um numero: '))
numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'Onze', 'Doze', 'Treze', 'Catorze ou Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while numero_informado < 0 or numero_informado > 20:
    numero_informado = int(input('Numero fora do intervalo! Tente novamento: '))

print('Você digitou o numero {}.'.format(numero_extenso[numero_informado].lower()))
print('*'*40)





# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 72: Crie um programa que tenha uma dupla 
totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo 
teclado (entre 0 e 20) e mostrá-lo por extenso.
"""