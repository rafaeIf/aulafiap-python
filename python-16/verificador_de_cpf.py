cpf = input('escreva o seu cpf: ')

#penultimo numero
y=0
for i in range (0, 9):
    x = int(cpf[i]) * (10-i)
    y = y + x 
print(y)
p_num = 11 - (y % 11)
if p_num >= 10:
    p_num = 0
print(p_num)

#ultimo numero
y=0
for i in range (0, 10):
    x = int(cpf[i]) * (11-i)
    y = y + x 
print(y)
u_num = 11 - (y % 11)
if u_num >= 10:
    u_num = 0
print(u_num)

if int(cpf[9]) == p_num and int(cpf[10]) == u_num:
    print('CPF VERDADEIRO')
else:
    print('CPF FALSO')