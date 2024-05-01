# multiplicação de uma matriz por um Escalar (k)
A = [
    [1, 2],
    [3, 4],
]
k = 2

for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        A[linha][coluna] *= k

for i in A:
    print(i)

print('')

# soma de duas matrizes
A = [
    [1, 2],
    [3, 4],
]
B = [
    [5, 6],
    [7, 8],
]
for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        A[linha][coluna] += B[linha][coluna]

for i in A:
    print(i)

print('')

# Multiplicação de Matrizes

A = [
    [1, 2],
    [3, 4],
]
B = [
    [5, 6],
    [7, 8],
]

AB = [
    [None, None],
    [None, None],
]

for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        if linha == 0 and coluna == 0:
            AB[linha][coluna] = (A[linha][coluna] * B[linha][coluna]) + (A[linha][coluna + 1] * B[linha + 1][coluna])
        elif linha == 0 and coluna == 1:
            AB[linha][coluna] = (A[linha][coluna - 1] * B[linha][coluna]) + (A[linha][coluna] * B[linha + 1][coluna])
        elif linha == 1 and coluna == 0:
            AB[linha][coluna] = (A[linha][coluna] * B[linha - 1][coluna]) + (A[linha][coluna + 1] * B[linha][coluna])
        else:
            AB[linha][coluna] = (A[linha][coluna - 1] * B[linha - 1][coluna]) + (A[linha][coluna] * B[linha][coluna])

for i in AB:
    print(i)