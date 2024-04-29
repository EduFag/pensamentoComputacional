# Notas de aula (22/04/2024 - Operadores lógicos e condições)
## Comentários em códigos
Ajudam no entendimento de trechos complexos
````
# Comentários
````
## Operadores lógicos
| A | B | not A | A and B | A or B |
| - | - | ----- | ------- | ------ |
|true |true |false |true |true |
|true |false |false |false |true |
|false |true |true |false |true |
|false |false |true |false |false |

## Operadores lógicos: precedências
Operações são executadas nesta ordem:
1. parênteses mais internos
2. not
3. and
4. or

## Operadores relacionais
Representam relação entre duas variáveis
- Igual a (==)
- Diferente de (!=)
- Maior que (>)
- Menor que (<)
- Maior ou igual a (>=)
- Menor ou igual a (<=)

## Comandos condicionais
### if
Executa um bloco de código apenas se a condição for verdadeira.
- Estrutura básica:
````
condition = true
print("before 'if'")
if condition:
    print("condition == True")
print("after 'if'")
````
### if-else
Executa o primeiro bloco de código se a condição for verdadeira, do contrário executa o segundo bloco.
- Estrutura básica:
````
x = 3
if x % 2 == 0:
    print("x é par")
else:
    print("x é ímpar")
````
### if-elif-else
Possibilita avaliar múltiplas condições, executando o primeiro bloco onde a condição for verdadeira. Caso nenhum bloco for verdadeiro, executa o bloco do else.
- Estrutura básica:
````
x = -42
if x > 0:
    print("x é positivo")
elif x < 0:
    print("x é negativo")
else:
    print("x é zero")
````
### match-case
- Possibilita fazer múltiplos ‘if’s de forma menos verbosa.
- O mesmo pode ser escrito com múltiplos ‘ifs’
- É um ‘syntactic sugar’
- Adicionado ao Python 3.10. 
- Conhecido como switch em outras linguagens.



