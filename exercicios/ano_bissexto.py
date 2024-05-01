ano = int(input('digite um ano: '))

if ano % 4 == 0:
    print('o ano é bissexto! ')
else:
    print('o ano não é bissexto')
    print('o próximo ano que será bissexto é', ano + (4 - ano % 4))