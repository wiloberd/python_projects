
# Este programa mostra o antecessor e 
# o sucessor de um numero digitado.

numero_digitado = int(input('Digite um numero: '))
antecessor = numero_digitado - 1
sucessor = numero_digitado + 1

print('O numero digitado é {}, seu antecessor é {} e seu sucessor é {}.'.format(numero_digitado, antecessor, sucessor))

# O bloco de codigo a seguir calcula o doblo, 
# o triplo e a raiz quadrada do numero.

double = numero_digitado * 2
triplo = numero_digitado * 3
raiz_quadrada = numero_digitado ** (1/2)

print('O double do numero digitado é {}, o seu triplo {}, a sua raiz quadrada é {}'.format(double, triplo, raiz_quadrada))