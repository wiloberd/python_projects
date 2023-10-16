mensagem = 'ANALIZADOR DE TRIANGULO - SMART'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

primeiro_segmento = int(input('Informe o primeiro segmento do triangulo: '))
segundo_segmento  = int(input('Informe o secundo segmento do triangulo: '))
terceiro_segmento  = int(input('Informe o terceiro segmento do triangulo: '))


if (primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento ):
    print('Os segmentos informado PODEM formar um triangulo', end=' ')
    if(primeiro_segmento == segundo_segmento and primeiro_segmento == terceiro_segmento and segundo_segmento == terceiro_segmento):
        print('EQUILÁTERO!')
    elif(primeiro_segmento == segundo_segmento or primeiro_segmento == terceiro_segmento or segundo_segmento == terceiro_segmento):
        print('ISÓSCELES!')
    elif( primeiro_segmento != segundo_segmento and segundo_segmento != terceiro_segmento and primeiro_segmento != terceiro_segmento):
        print('ESCALENO!')
else:
    print('\033[0;31mOs segmentos informado NÃO PODEM formar um triangulo.\033[m')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 42: Refaça o DESAFIO 35 dos 
triângulos, acrescentando o recurso de mostrar 
que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""