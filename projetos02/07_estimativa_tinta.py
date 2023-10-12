# Este programa faz uma estimativa da quantidade de 
# tinta necessaria para pinta uma parede após
# calcular a sua areia.
# sabendo que 1L de tinta pinta 2m^2
# e 1L de tinta comum é custa R$ 52.00 

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

# calculando a superficia da parede
area = largura * altura

# calculando a quantidade necessária de tinta de acordo com a area calculada.
if (area % 2 != 0):
    # se a area for um valor decimal, adiciona 1 na parte inteira.
    quantidade_tinta = (area // 2) + 1
else:
    # senão divide a area por 2 para determinar a quantidade total em litro.
    quantidade_tinta = (area / 2)

# calculando a quantidade total de dinheiro necessária para o projeto.
valor_total = quantidade_tinta * 52
print('A area da sua parede é {:.2f} metro quadrado e tem uma dimensão de {:.1f}x{:.1f}.'.format(area, largura, altura))

print('Você precisará de {:.0f}l de tinta'.format(quantidade_tinta), end=" ")
print('e de R${:.2f} BRL de investimento em tinta.'.format(valor_total))
