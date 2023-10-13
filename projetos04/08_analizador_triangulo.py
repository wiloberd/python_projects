mensagem = 'ANALIZADOR DE TRIANGULO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

primeiro_segmento = int(input('Informe o primeiro segmento do triangulo: '))
segundo_segmento  = int(input('Informe o secundo segmento do triangulo: '))
terceiro_segmento  = int(input('Informe o terceiro segmento do triangulo: '))


if (primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento ):
    print('Os segmentos informado PODEM formar um triangulo.')
else:
    print('Os segmentos informado NÃO PODEM formar um triangulo.')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 35: Desenvolva um programa que leia o 
comprimento de três retas e diga ao usuário se elas podem 
ou não formar um triângulo.
"""