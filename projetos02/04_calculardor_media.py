# Este programa leia e calcule e mostre a media entre
# duas notas de um aluno.
mensagem = 'CALCULADOR DE MÉDIA ARITMETICA'
print('*'*40)
print('{:^40}'.format(mensagem))
print('*'*40)

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media_aritmetica = (primeira_nota + segunda_nota) / 2

print('A média entre {} e {} é igual a: {:.1f}'.format(primeira_nota, segunda_nota, media_aritmetica))