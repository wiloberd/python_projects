mensagem = 'TABUADA'
print('*'*20)
print('{:^20}'.format(mensagem))
print('*'*20)

tabua = 2

for posicao in range(1, 11):
    print(' {} x {} = {}'.format(tabua, posicao, (tabua*posicao)))
    
print('*'*15)


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando 
a tabuada de um número que o usuário escolher, só 
que agora utilizando um laço for.
"""