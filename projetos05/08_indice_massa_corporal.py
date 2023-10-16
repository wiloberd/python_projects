from math import pow

mensagem = 'INDICE MASSA CORPORAL'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

peso_informado = float(input('Informe seu peso (Kg): '))
altura_informada = float(input('Informe sua altura (m): '))

imc = peso_informado / pow(altura_informada, 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if (imc < 18.5):
    print('ATENÇÃO! Você esta na faixa', end=' ')
    print('Abaixo do Peso')
elif (imc > 18.5 and imc <= 25):
    print('PARABÉNS! Você esta na faixa de', end=' ')
    print('Peso Ideal')
elif (25 < imc <= 30):
    print('ATENÇÃO! Você esta na faixa de', end=' ')
    print('Sobrepeso')
elif (30 < imc <= 40):
    print('ATENÇÃO! Você esta na faixa de', end=' ')
    print('Obesidade')
else:
    print('ATENÇÃO! Você esta na faixa de', end=' ')
    print('Obesidade Mórbida')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 43: Desenvolva uma lógica que 
leia o peso e a altura de uma pessoa, calcule 
seu Índice de Massa Corporal (IMC) e mostre 
seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""