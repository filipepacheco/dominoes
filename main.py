# Lê um arquivo e formata ele em uma lista de lista de dominós
def read_file(name='in3'):
    f = open(f'test_cases/{name}', "r")
    # Lista de lista dominós
    dominoes_input = []

    dominoes_size = int(f.readline())
    while dominoes_size > 0:
        # Lista de dominós
        dom = []
        for i in range(0, dominoes_size):
            line = f.readline().rstrip('\n')
            value = tuple(int(x) for x in line.split(" "))
            # Cada dominó é um DICT formado por value e metadata
            # Value é uma tupla contendo a posição de cima e a posição de baixo (cima, baixo)
            domino = {
                "value": value,
                "metadata": get_domino_metadata(value)
            }
            dom.append(domino)

        # Uma lista de dominós é formada por value e metadata
        # value é uma lista contando todos os dominós
        dominoes_input.append({
            "value": dom,
            "metadata": get_dominoes_metadata(dom)
        })
        dominoes_size = int(f.readline())

    return dominoes_input


def get_domino_metadata(value):
    return {
        "diff": value[0] - value[1],  # a diferença de cima - baixo
        "diff_odd": (value[0] - value[1]) % 2 == 0,  # se a diferença é par ou ímpar
        "diff_by_two": (value[0] + value[1]) / 2,  # a soma dividida por 2
        "diff_swap": 2 * (value[0] - value[1]),  # o peso desse dominó caso aconteça o swap
    }


def get_dominoes_metadata(dom):
    sum_d = sum_dominoes(dom)
    return {
        "sum_down": sum_d[0],  # A soma de todas as partes de cima dos dominós
        "sum_up": sum_d[1],  # A soma de todas as partes de baixo dos dominós
        "total_sum": sum_d[0] + sum_d[1],  # soma de cima + soma de baixo
        "difference": sum_d[0] - sum_d[1],  # diferença entre a soma de cima e a de baixo
        "sum_has_module": (sum_d[0] + sum_d[1]) % 2,  # Se a soma de cima + soma de baixo é par ou impar
    }


# Recebe uma lista de dominos e soma a parte de cima, a parte de baixo, e retorna numa tupla
def sum_dominoes(d):
    sum_up, sum_down = 0, 0
    for domino in d:
        sum_up += domino['value'][0]
        sum_down += domino['value'][1]
    return sum_up, sum_down


# Retorna todos os dominós cuja diferença entre cima-baixo seja ímpar
def get_diff_odd(dominoes_list):
    return [d for d in dominoes_list if not d['metadata']['diff_odd']]


# Remove um dominó a partir de duas condições
# 1. O dominó possui uma diferença cima-baixo impar
# 2. O dominó possui a soma menor dividida por 2 entre os diferença ímpares
def remove_lowest_value_index(dominoes_list):
    diff_odds = get_diff_odd(dominoes_list)
    lowest_domino = min(diff_odds, key=lambda x: x['metadata']['diff_by_two'])
    lowest_value_index = dominoes_list.index(lowest_domino)

    del dominoes_list[lowest_value_index]
    del lowest_value_index
    del diff_odds

    return dominoes_list, lowest_domino["value"]


import random


# Busca o dominó cujo diff_swap mais se aproxima do diff da lista de dominós
def get_closest_index(dominoes_list, diff):
    index = dominoes_list.index(min(dominoes_list, key=lambda x: abs(x['metadata']['diff_swap'] - diff)))

    # Se o dominó encontrado encontra um dominó que já realizou um swap, significa que o algoritmo ficou viciado.
    # Para impedir que ele fique em loop inifinito, é designado um novo dominó aleatório para começar os swaps do zero
    # E limpa o array de dominós swapped
    if index in swapped_indexes:
        index = random.randrange(0, len(dominoes_list))
        reset_swapped_indexes()

    return index


# Recebe a lista de dominós e o índice do dominó que será invertido
def swap_domino(dominoes_list, index):
    dom = dominoes_list[index]["value"]
    dominoes_list[index]["value"] = (dom[1], dom[0])
    # Recalcula os metadados para esse dominó invertido
    dominoes_list[index]["metadata"] = get_domino_metadata((dom[1], dom[0]))

    return dominoes_list[index]


def update_metadata(dominoes_list):
    return get_dominoes_metadata(dominoes_list)


# Lista de índices que já realizaram o swap
swapped_indexes = []


# Caso necessário, a lista de índices é reinicializada do zero
def reset_swapped_indexes():
    swapped_indexes = []


import sys

try:
    input_file = sys.argv[1]
    dom_input = read_file(input_file)
except IndexError:
    input_file = 'in3'
    dom_input = read_file(input_file)

import time

# Varre a lista de lista de dominós
for dominoes_with_metadata in dom_input:
    # Faz uma cópia dos dominós em variáveis locais, visto que listas em Python são ponteiros e podem ter o valor
    # Alterado de maneira não intencional
    dominoes = dominoes_with_metadata['value'].copy()
    metadata = dominoes_with_metadata['metadata'].copy()
    lowest_value = None

    # Verifica se a lista de dominós atual possui uma soma total ímpar
    if metadata["sum_has_module"] == 1:
        # Se sim, então escolhe um dominó para remover
        dominoes, lowest_value = remove_lowest_value_index(dominoes)

    start_time = time.time()
    # Loop até encontrar a solução
    while True:
        # Atualiza os metadados da lista de dominós atual
        metadata = update_metadata(dominoes)

        # Se a diferença entre soma cima - soma baixo for 0, significa que os lados estão iguais
        # E o algoritmo deve ser finalizado
        if metadata["difference"] == 0:
            if lowest_value:
                print(metadata["sum_up"], "descartado dominó", lowest_value)
            else:
                print(metadata["sum_up"], "nenhum dominó descartado")
            break

        # Se demorou mais do que 10 segundos para executar, consideramos que é impossível de resolver.
        if time.time() - start_time > 10:
            print("impossível")
            break

        # Busca o dominó cujo diff_swap mais se aproxima do diff da lista do metadata de dominós
        closest_index = get_closest_index(dominoes, metadata["difference"])
        # Realiza o swap no dominó encontrado
        dominoes[closest_index] = swap_domino(dominoes, closest_index)
        # Registra esse índice na lita de swapped indexes
        swapped_indexes.append(closest_index)
