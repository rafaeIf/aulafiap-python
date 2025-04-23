def funcao_com_parametro_kwargs(**kwargs):
    print(kwargs['nome']) # se não tiver nome vai dar erro
    print(kwargs.get('nome')) # se não tiver é None

funcao_com_parametro_kwargs(valor=1, nome='rafael')