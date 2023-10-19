from time import sleep

mensagem_inicial = 'CALCULADOR UNIVERSAL'
mensagem_menu = 'MENU'
print('*'*40)
print('{:^40}'.format(mensagem_inicial))
print('*'*40)

primeiro_numero = float(input('Informe o primeiro numero: '))
segundo_numero = float(input('Informe o segundo numero: '))

opcao = 0
while opcao != 5:
    print('*'*20)
    print('{:^20}'.format(mensagem_menu))
    print('*'*20)
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
""")
    opcao = int(input('Qual é sua opação : '))


    if opcao == 1:
        soma = primeiro_numero + segundo_numero
        print('A soma de {:.0f} + {:.0f} = {:.0f}.'.format(primeiro_numero, segundo_numero, soma))
    elif opcao == 2:
        produto = primeiro_numero * segundo_numero
        print('O produto de {:.0f} x {:.0f} = {:.0f}.'.format(primeiro_numero, segundo_numero, produto))
    elif opcao == 3:
        print(' {:.0f} é maior que {:.0f}'.format(primeiro_numero, segundo_numero) if primeiro_numero > segundo_numero else '{:.0f} é maior que {:.0f}'.format(segundo_numero, primeiro_numero))
    elif opcao == 4:
        primeiro_numero = float(input('Informe o primeiro novo numero: '))
        segundo_numero = float(input('Informe o segundo novo numero: '))
    elif opcao != 0 and opcao != 5:
        print('\033[0;31mInforme uma opação valida!\033[m')
        



print('Saindo do programa...')
sleep(1)
print('*'*30)
print('Obrigado por usar o programa!\n')




# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 059: Crie um programa que leia dois valores 
e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""