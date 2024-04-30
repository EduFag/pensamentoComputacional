import random

lista = []

# gerando lista aleatória
for i in range(10):
    lista.append(random.randint(0, 20))

print('lista antes da ordenação:', lista)

# n = comprimento da lista
n = len(lista)

# laço de repetição para ordenar todos os elementos da lista
for i in range(n):
    # laço de repetição que verifica a condição para todos os elementos da lista
    for j in range(n - 1):
        # verifica se um numéro é maior que seu sucessor
        if lista[j] > lista[j + 1]:
            # inverte a posição dos números
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print('lista depois da ordenação:', lista)