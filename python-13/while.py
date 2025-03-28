impares = [1, 3, 5, 7, 9]
pares = [i + 1 for i in impares] # filosofar

print(pares)

x = 0

while x < 5:
    print(x)
    x+=1

while len(impares) > 0:
    var = impares.pop()
    print(var + 1)

lista = [1,2,3,4,5,6,7,8,9,10]
while lista:
    x = lista.pop(0) #tirando o primeiro termo
    print(x)
    if x % 5 == 0:
        break  