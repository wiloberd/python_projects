mensagem = 'TABUADA'
print('*'*35)
print('{:^35}'.format(mensagem))
print('*'*35)

resposta = 'S'
tabuada = int(input('Quer ver a tabuada de qual numero: '))

while resposta == 'S':
    if tabuada < 0:
        print('*'*35)
        print('Valor digitado inferior a zero!')
        print('Obrigado por usar o programa!')
        print('*'*35)
        break
    else:
        for posicao in range(1, 11):
            print(' {} x {} = {}'.format(tabuada, posicao, (tabuada*posicao)))
        resposta = str(input('Gostaria ver mais uma tabuada S/N:: ')).upper().strip()[0]
        if resposta == 'S':
            tabuada = int(input('Quer ver a tabuada de qual numero: '))
        else:
            print('*'*35)
            print('Obrigado por usar o programa!')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 67: Faça um programa que mostre a tabuada de 
vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
"""