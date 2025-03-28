import time
import random

seed = random.randint(1, 99)
rm = '154262'
print("numero aleatorio: ",seed)

for i in range(30):
    print(i, end=', ')
    time.sleep(0) # coloca os segundos

cadastro = {
    'nome': 'vagner',
    'idade': 39,
    'peso': 65.5,
    'altura': 1.70,
    'usuario_python': True
}

for i in cadastro.values(): # values, keys, items
    print(i)