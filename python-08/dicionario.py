dicionario = {
    'nome':'vagner',
    'idade':39,
    'peso':67.2,
    'altura':1.7,
    'python_user':True
}

print(dicionario['altura'])
print(dicionario['peso']/dicionario['altura'])
print(dicionario.keys()) #todas as chaves: nome, idade
print(dicionario.values()) #todos os valores: vagner, 39
print(dicionario.items()) #pares

print(dicionario.get('nome')) #ele retorna o valor pela chave