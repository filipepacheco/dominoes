# Lê um arquivo e formata ele em um array de arrays com os dominós
def read_file(name='in3'):
    f = open(f'test_cases/{name}', "r")
    dominoes = []
    dominoes_size = int(f.readline())
    while dominoes_size > 0:
        dom = []
        for i in range(0, dominoes_size):
            line = f.readline().rstrip('\n')
            domino = tuple(int(l) for l in line.split(" "))
            dom.append(domino)
        dominoes_size = int(f.readline())
        dominoes.append(dom)

    return dominoes


# Recebe um inteiro e transforma numa string binaria, depois numa lista e preenche com zeros a esquerda
def int_to_bin(i, size):
    i = bin(i).replace('-0b', '').replace('0b', '').zfill(size)
    list1 = []
    list1[:0] = i
    return list1


# Soma a parte de cima dos dominos, a parte de baixo, e retorna numa tupla
def sum_dominoes(dominoes):
    sum_up, sum_down = 0, 0
    for domino in dominoes:
        sum_up += domino[0]
        sum_down += domino[1]
    return sum_up, sum_down


def swap_domino(y):
    return y[1], y[0]


def swap_dominoes(original_dominoes, current_swap, dominoes_size):
    # Transforma o número da iteração atual current_swap em um número binário e depois em uma lista
    # Exemplo: se o dominoes_size = 4 e current_swap = 2, ele vai transformar em ["0", "0", "1", "0"]
    # Nesse array de current_swap, teremos 4 posições correspondentes a cada um dos dominós.
    # Se no current_swap o valor é = "1", significa que essa posição receberá o swap
    current_swap = int_to_bin(current_swap, dominoes_size)
    # Faz uma cópia para manter o array de dominós original e não sobrescrever com os swaps

    dom = original_dominoes.copy()
    for i, should_swap in enumerate(current_swap):
        if should_swap == '1':
            dom[i] = swap_domino(original_dominoes[i])
    return dom


def swap_until_equal(original_dominoes):
    removed_dominoes = original_dominoes
    removed_domino = -1
    found = False

    while True:
        # Retorna um número binario e converte ele para inteiro.
        # Exemplo: se são 4 dominós, ele retorna '1111', e transforma no niumero inteiro 16
        # 5 dominós = '11111' = 32, etc.
        dominoes_size = len(removed_dominoes)
        max_swaps = int(''.ljust(dominoes_size, '1'), 2)
        current_swap = 0

        while True:
            sum_d = sum_dominoes(removed_dominoes)
            if (sum_d[0] + sum_d[1]) % 2 != 0:
                break
            # Se a soma de cima e a de baixo forem iguais, encerra o programa
            if sum_d[0] == sum_d[1]:
                print(sum_d[0], end=" ")
                found = True
                break
            removed_dominoes = swap_dominoes(removed_dominoes, current_swap, dominoes_size)

            # Senão, continua até chegar no limite maximo de swaps
            current_swap += 1
            if current_swap >= max_swaps:
                break

        if found:
            break

        removed_domino += 1

        if removed_domino >= dominoes_size:
            print('impossivel')
            break

        removed_dominoes = original_dominoes.copy()
        removed_dominoes.pop(removed_domino)

    if found:
        if removed_domino >= 0:
            print('descartado ', original_dominoes[removed_domino])
        else:
            print('nenhum dominó descartado')


dominoes_list = read_file()

# Itera sobre a lista de dominós e realiza os swaps até encontrar a soma igual
for x in dominoes_list:
    swap_until_equal(x)
