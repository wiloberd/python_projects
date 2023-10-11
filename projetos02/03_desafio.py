
# Este programa mostra o antecessor e 
# o sucessor de um numero digitado.

numero = int(input('Digite um numero: '))
antecessor = numero - 1
sucessor = numero + 1

print('O numero digitado é {}, seu antecessor é {} e seu sucessor é {}.'.format(numero, antecessor, sucessor))

# O bloco de codigo a seguir calcula o doblo, 
# o triplo e a raiz quadrada do numero.

double = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print('O double do numero digitado é {}, o seu triplo {}, a sua raiz quadrada é {}'.format(double, triplo, raiz_quadrada))