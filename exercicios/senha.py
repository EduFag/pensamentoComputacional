senha = '6'
tent = 1
resp = input('digite a senha: ')

while resp != senha:
    print('senha errada!')
    tent += 1
    resp = input('digite a senha correta: ')

print('acesso liberado!')
print('total de tentativas:', tent)