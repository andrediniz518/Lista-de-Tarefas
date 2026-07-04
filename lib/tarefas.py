from lib.interface import leiaInt


def adicionar_tarefa(lista):
    """
    -> Função designada para adicionar tarefas e o status dentro da lista
    :param lista: recebe a lista de tarefas
    """
    nome_tarefa = str(input('Nome da tarefa: '))
    tarefa = []
    tarefa.append(nome_tarefa)
    tarefa.append(False)
    lista.append(tarefa)
    print('Tarefa adicionada com Sucesso!')


def listar_tarefas(lista):
    """
    -> função designada para listar no prompt, a lista e o status
    da tarefa: andamento ou finalizada
    :param lista: recebe a lista de tarefas
    """
    if len(lista) != 0:
        print('TAREFAS'.center(42))
        c = 1
        for item in lista:
            print(f'{c} - {item[0]} | STATUS: ', end='')
            if item[1] == True:
                print('finalizada')
            else:
                print('andamento')
            c += 1
    else:
        print('lista de tarefas vazia. Adicione para poder visualizar.')


def concluir_tarefa(lista):
    """
    -> função designada para marcar como concluída a tarefa pelo
    qual o usuario informar, mundando o  status para finalizada.
    :param lista: recebe a lista de tarefas
    """
    if len(lista) != 0:
        listar_tarefas(lista)
        while True:
            resp = leiaInt('Finalizar qual tarefa? ')
            if resp > 0 and resp <= len(lista):
                if lista[resp-1][1]:
                    print('Tarefa já finalizada! Tente outra tarefa.')
                    continue
                else:
                    lista[resp-1][1] = True
                    print('Tarefa finalizada com sucesso!')
                    break
            else:
                print('Digite uma opção valida acima.')
    else:
        print('lista de tarefas vazia. Adicione para poder concluir.')

def remover_tarefa(lista):
    """
    -> função designada para remover tarefas da lista seja ela
    no status: andamento ou finalizada.
    :param lista: recebe a lista de tarefas
    """
    if len(lista) == 0:
        print('lista de tarefas vazia. Adicione para poder remover.')
    else:
        listar_tarefas(lista)
        while True:
            resp = leiaInt('Remover qual tarefa? ')
            if resp > 0 and resp <= len(lista):
                removido = lista.pop(resp-1)
                print(f'A tarefa \'{removido[0]}\' foi removido com sucesso!')
                break
            else:
                print('Digite uma opção valida acima.')