from lib.interface import *
from lib.tarefas import *

cabeçalho('LISTA DE TAREFAS v1.0')
tarefas = []


while True:
    resp = menu(['Adicionar tarefa', 'Ver tarefas', 'Concluir tarefa', 'Remover tarefa', 'Sair'])
    if resp == 1:
        adicionar_tarefa(tarefas)
    elif resp == 2:
        listar_tarefas(tarefas)
    elif resp == 3:
        concluir_tarefa(tarefas)
    elif resp == 4:
        remover_tarefa(tarefas)
    elif resp == 5:
        print('Saindo!')
        break
    else:
        print('Digite uma opção válida acima!')

