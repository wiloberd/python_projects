
# print personalizado
nome = input('Qual é seu nome: ')

# conteudo da variavel alinhado a centralizado.
print('Prazer te conhecer:{:^20}!'.format(nome))
# conteudo da variavel alinhado a centralizado.
print('Prazer te conhecer:{:-^20}!'.format(nome))
# conteudo da variavel alinhado a direita.
print('Prazer te conhecer:{:>20}!'.format(nome))