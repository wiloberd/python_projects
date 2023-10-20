mensagem = 'ANLISADOR DADOS'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

contador_nove = 0
numero_par = ()

tupla_numero = (int(input('Digite um numero: ')), int(input('Digite um outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite mais um outro numero: ')), int(input('Digite o ultimo numero: ')) )

print('*'*40)

print('O numero 9 apareceu {} vezes'.format(tupla_numero.count(9)))
print('O primeiro valor 3 foi digitado na {}º posição'.format(tupla_numero.index(3) + 1) if (tupla_numero.count(3) > 0) else 'O valor 3 não está na tupla'  )


print('Os numeros pares foram: '.format(numero_par), end= "")
for index , element in enumerate(tupla_numero):
    if tupla_numero[index] % 2 == 0:
        print(element, end=' ')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 075: Desenvolva um programa que leia quatro 
valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""