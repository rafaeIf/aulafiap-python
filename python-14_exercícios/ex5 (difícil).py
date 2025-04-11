termo1 = 0
termo2 = 1
print(termo1)
print(termo2)
for i in range(1, 9):
    termo3 = termo1 + termo2
    print(termo3)
    termo1 = termo2
    termo2 = termo3
    