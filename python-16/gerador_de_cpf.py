import random
cpfValido = False
y=0

while not cpfValido:

    cpf = str(random.randint(10000000000, 99999999999))

    y=0
    for i in range (0, 9):
        x = int(cpf[i]) * (10-i)
        y = y + x 
        p_num = 11 - (y % 11)
    if p_num >= 10:
        p_num = 0

    y=0
    for i in range (0, 10):
        x = int(cpf[i]) * (11-i)
        y = y + x 
        u_num = 11 - (y % 11)
    if u_num >= 10:
        u_num = 0

    if int(cpf[9]) == p_num and int(cpf[10]) == u_num:
        cpfValido = True
        print(cpf)
    else:
        cpfValido = False