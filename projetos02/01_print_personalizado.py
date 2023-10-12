
# print personalizado
nome_usuario = input('Qual é seu nome: ')

# conteudo da variavel alinhado a centralizado.
print('Prazer te conhecer:{:^20}!'.format(nome_usuario))
# conteudo da variavel alinhado a centralizado.
print('Prazer te conhecer:{:-^20}!'.format(nome_usuario))
# conteudo da variavel alinhado a direita.
print('Prazer te conhecer:{:>20}!'.format(nome_usuario))