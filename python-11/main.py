idade = 62

match idade:
    case 60:
        print(60)
    case 50:
        print(50)
    case _:
        print("Outros")

classificacao = 'vip' if idade > 60 else 'normal'
print(classificacao)