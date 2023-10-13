mensagem = 'RADAR ELETRONICO'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

velocidade_informada = float(input('Informe a velocidade do carro: '))

aviso_multado = 'Você foi multado por ultrapassar 80km/h' if velocidade_informada > 80 else 'você está na velocidade normal. Ótima viagem!'

multa_total = 7 * (velocidade_informada - 80)

print('{}, e deverá pagar R${:.2f} de multa.'.format(aviso_multado, multa_total) if velocidade_informada > 80 else 'Sua velocidade é de {:.1f}km/h, e {}'.format(velocidade_informada, aviso_multado))


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
"""