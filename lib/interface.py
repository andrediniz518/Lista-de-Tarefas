def leiaInt(texto):
   """
   -> responsavel por validar dados inteiros somente.
   :param texto: o texto a ser mostrado ao usuario
   :return: retorna o valor inteiro validado ou -1 em casos
   de erro inesperado.
   """
   valida = True
   while valida:
       try:
           num = int(input(texto))
       except ValueError:
           print(f'Erro: por favor, digite um número inteiro válido')
           continue
       except KeyboardInterrupt:
           print(f'Entrada de dados interrompida pelo usuário.')
           return -1
       else:
           return num


def linha():
    """
    -> função para criar linhas de forma a agilziar o processo.
    """
    print('-' * 42)


def cabeçalho(texto):
    """
    -> função para criar um cabeçalho simples.
    :param texto: recebe o texto a ser exibido no cabeçalho
    """
    linha()
    print(texto.center(42))
    linha()


def menu(item_menu):
    """
    -> exibi o menu principal com todas as opções disponiveis,
    recebe a opção escolhida pelo usuario e retorna o valor
    :param item_menu: recebe uma lista com as opções disponiveis
    :return: retorna o numero escolhido pelo usuario
    """
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in item_menu:
        print(f'{c} - {item}')
        c += 1
    linha()
    resp = leiaInt('Sua opção: ')
    linha()
    return resp

