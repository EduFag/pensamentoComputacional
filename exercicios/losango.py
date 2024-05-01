altura = int(input('digite um número ímpar para formar um losango: '))

metade = altura // 2
# Desenha a metade superior, incluindo até a linha mais larga
for i in range(metade + 1):
    qtd_espacos = metade - i
    qtd_star = (2 * i) + 1
    print(' ' * qtd_espacos + '#' * qtd_star)

# Desenha a metade inferior
for i in range(metade):
    qtd_espacos = i + 1
    qtd_star = (altura - 2) - (2 * i)
    print(' ' * qtd_espacos + '#' * qtd_star)