# Anotações de aula (16/04/2024 - introdução ao python | variáveis e operadores matemáticos)
## Convenções em nomenclaturas

Convenções são práticas não obrigatórias de
desenvolvimento. São padrões da indústria que devem ser
seguidos.

- snake_case 🐍: usado para nome de variáveis. Letras minúsculas, separando palavras com ‘_’

````
user_name = "Eduardo"
total_amount = 1000
````

- CamelCase (a.k.a. PascalCase) 🐫: usado para nomes de classes.

````
class User:
    pass
````

- Constantes: letras maiúsculas, com ‘_’ separando palavras

````
MAX_VALUE = 100
PI_VALUE = 3.14
````

- Palavras reservadas: não nomeie variáveis com termos que possuem significado próprio no python


## Tipos de Dados


- numéricos
    - int: inteiros
    - float: racionais

- dados booleanos
    - bool: True ou False

- none 
    - None: ausência de informacão

- string
    - str: conjunto de caracteres (aspas duplas ou simples)

- listas
    - list: Coleção mutável e ordenada de itens.

- tupla
    - tuple: Coleção imutável e ordenada de itens.

- dicionário
    - Conjunto mutável de pares chave-valor (key-value).

- conjuntos
    - set: Grupo mutável e não-ordenado de itens únicos

- conjuntos congelados
    - frozenset: Grupo não-mutável e não-ordenado de itens únicos.

<br><br>

Use o método type para confirmar o tipo de uma
variável

````
>>> type(variável)
<class 'tipo da variável'>
````

## Operadores matemáticos

- adição ( + )
- subtração ( - )
- multiplicação ( * )
- divisáo ( / )
- quociente inteiro da divisão ( // )
- resto da divisão ( % )
- exponenciacão ( ** )

## Exercício de aula

````
L = int(input("digite a largura do retângulo:"))
A = int(input("digite a altura do retângulo:"))

area = L*A
perimetro = 2*(L+A)
hipotenusa = (L**2 + A**2)**(1/2)

print("área do retângulo =", area)
print("Perímetro do retângulo =", perimetro)
print("Hipotenusa do retângulo =", hipotenusa)

````