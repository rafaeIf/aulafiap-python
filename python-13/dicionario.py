cadastro = {
    'nome' : 'r. jonberson',
    'idade' : 43,
    'programador' : True,
    'linguagens': [
        'python',
        'go',
        'java',
        'c#'
    ]
}

for key, value in cadastro.items():
    if type(value) is list:
        print(key,':')

        for i in value:
            print('\t',i)
    else:
        print(key,': ',str(value))