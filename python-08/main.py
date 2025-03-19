lista_numerica = [1,2,3]
lista_texto = ['a','b','c']
lista_decimal = [1.2, 1.3, 1.4]
lista_boolean = [True, False, True]

print(lista_numerica)
print(lista_texto)
print(lista_decimal)
print(lista_boolean)

print(lista_numerica[0], lista_numerica[0:3], lista_numerica[:-1])
lista_numerica[0] = 68
print(lista_numerica)
x = lista_numerica[0]+lista_numerica[2]
print(x)

lista_numerica.append(9) # adiciona na lista um novo index
print(lista_numerica)
lista_numerica.pop() # tira o indice padrão (é o ultimo)

tupla = (1, 2, 3)
conjuntos = {3, 2, 2, 1, 10, 5, 5, 7}
conjuntos2 = {3, 5, 100, 43}
print(conjuntos) # ele ordena e tira repetições
print(conjuntos.intersection(conjuntos2))
print(conjuntos.difference(conjuntos2))

lista_aninhada= [[1, 3, 0], #matriz
                 [3, 6, 5],
                 [8, 9, 7]]
print(lista_aninhada[1][1])