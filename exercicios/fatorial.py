n = int(input('digite um número para calcular seu fatorial: '))
n_inicial = n

for i in range(1, n):
    n *= i
print(n_inicial,'! =', n)