mensagem = 'VALIDAÇÃO DE EXPRESSÃO ARITMETICA'
print('*'*50)
print('{:^50}'.format(mensagem))
print('*'*50)

parentese_aberto = []
parentese_fechado = []

expressao = str(input("Informe a expressão: "))

for element in expressao:
    if element == '(':
        parentese_aberto.append(element) 
    elif element == ')':
        parentese_fechado.append(element)

if (len(parentese_aberto) != len(parentese_fechado)):
    print('Sua expressão está erradaaa!')
    print('Posui um parênteses a mais')
else:
    print('Sua expressão está correta!')
    

# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 083: Crie um programa onde o usuário digite uma 
expressão qualquer que use parênteses. Seu aplicativo deverá 
analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.
"""