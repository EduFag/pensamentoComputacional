l = int(input('digite a largura do retângulo: '))
h = int(input('digite a altura do retângulo: '))

area = l * h
perimetro = (l + h) * 2
hipotenusa = (l ** 2 + h ** 2) ** 0.5

print('área do retângulo:', area)
print('perímetro do retângulo:', perimetro)
print('hipotenusa do retângulo:', hipotenusa)