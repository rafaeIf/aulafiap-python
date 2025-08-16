'''
file = open('teste.txt') #abre o arquivo / seleciona
texto = file.readline() #lê a primeira linha
print(texto) #mostra a primeira linha
'''

'''
file = open('teste.txt', mode='w') #abre no modo reescrita
#mode a = append (adiciona texto)
#mode x = cria um novo arquivo (se ele nao existir)
file.write('rafael') #escreve rafael
file.write('\nlinha 2') #escreve linha 2 na linha 2
file.close() #fecha o arquivo e o modo
file = open('teste.txt')
texto = file.read() #le tudo
print(texto)
'''

#split pega palavra por palavra e divide numa lista
#join pega as palavras e junta em uma só
#flush salva no disco os dados do buffer (tipo um backup)


