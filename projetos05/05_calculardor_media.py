mensagem = 'CALCULADOR DE MÉDIA ARITMETICA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media_aritmetica = (primeira_nota + segunda_nota) / 2

if (media_aritmetica >= 7):
    print('Sua média foi: {:.1f}, APROVADO!'.format(media_aritmetica))
    print('PARABÉNS!')
elif (  media_aritmetica >= 5 and media_aritmetica < 7):
     print('Sua média foi: {:.1f}, em RECUPERAÇÃO!'.format(media_aritmetica))
     print('ESTUDE MAIS!')
elif (media_aritmetica < 5):
    print(f'Sua médoa foi {media_aritmetica} e foi REPROVADO')
    print('Dicas: Na proxima vai dar certo!')



# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 040: Crie um programa que leia duas notas 
de um aluno e calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""