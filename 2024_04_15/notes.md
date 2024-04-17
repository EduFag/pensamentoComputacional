# Notas de aula (15/04/2024 - python e linguagens de programação)

## Linguagens de programação
Controle de fluxo de execução é o que define uma linguagem de programação

Quando usar cada uma ? <br>
Considere critérios técnicos, como:
- Requisitos do projeto
- Ecossistema existente (bibliotecas)
- Custos de licença (se houver)
- Perfil de equipe e disponibilidade no mercado

## História do Python

- Criada por Guido van Rossum 
    - Engenheiro @ Microsoft, Dropbox, Google...
- Primeira versão em 1991

## A linguagem Python
- Wikipedia explica como: Python is a high-level [1], general-purpose [2] (...), interpreted[3] programming language. (...) emphasizes code readability[4] with the use of significant indentation[4]. Python is dynamically typed[5] and garbage-collected[6]. (...)

### [1] - Linguagens de Alto Nível

- Projetadas para serem mais próximas da linguagem humana.
- São independentes da arquitetura de hardware em que
executarão (o mesmo código executa em diferentes ambientes).
- Normalmente oferecem abstrações para tarefas complexas, como manipulação de strings, gestão de memória e I/O (entrada/saída).
    - Exemplos: Python, Java, C#, JavaScript, Ruby.

### [1] - Linguagens de Baixo Nível

- São mais próximas da linguagem de máquina e do hardware que executará (mais difíceis de entender e de programar).
- São mais dependentes do hardware que executarão
- Oferecem um maior controle sobre os recursos de baixo nível,
como memória e processador.
- São usadas onde é necessário muito desempenho ou controle próprio de hardware.
    - Exemplos: Assembly.

### [2] - Linguagens de Propósito Geral

- São projetadas para serem aplicáveis em uma ampla variedade de problemas e contextos (jogos, web, mobile, IA...).
- Oferecem recursos e abstrações que podem ser utilizados para desenvolver soluções para múltiplos domínios.
- Tendem a ser mais versáteis e com uma base de usuários maior.
    - Exemplos: C, C++, Java, Python, JavaScript e Ruby.

### [2] - Linguagens de Domínio Específico
Também chamadas de DSL (Domain Specific Languages)

- Projetadas para resolver problemas em um domínio particular.
- Otimizadas para lidar com tarefas específicas dentro de uma área. 
- Frequentemente combinadas com linguagens de propósito geral.

### [3] - Compilação ou interpretação

| Características | Linguagens Compiladas | Linguagens Interpretadas |
| --------------- | --------------------- | ------------------------ |
| Execução | O código é convertido em código de máquina e executado diretamente pela CPU. | O código é traduzido linha por linha e executado por um interpretador.
| Desempenho | Geralmente velocidade de execução mais rápida, pois o programa inteiro é pré-compilado. | A velocidade de execução pode ser mais lenta, já que o código é traduzido durante a execução. |
| Portabilidade | Normalmente menos portáteis, já que os binários são especificos para a plataforma alvo. | Geralmente mais portáteis, pois o interpretador pode ser executado em diferentes plataformas. |
| Desenvolvimento | Tempos de compilação mais longos, mas os erros são identificados antes da execução. | Feedback instantâneo sobre erros de sintaxe e depuração mais fácil. |
| Uso de memória | O código compilado geralmente requer menos memória, pois não precisa do interpretador. | O código interpretado pode exigir mais memória devido à sobrecarga do interpretador. |
| Exemplos | C, C++, Rust, Go | Python, Ruby, JavaScript, PHP |

<br>
linguagem compilada --> CPU
linguagem interpretada --> interpretador --> CPU 

### [4] - Legibilidade e identação

- Formatação visual do código
- A indentação desempenha um papel fundamental na legibilidade do código.
- Serve para podermos entender a estrutura e lógica do código.
- A identação do Python é feita com espaços.

### [5] - Dynamically typed

- Dinamicamente tipado : (e.g. Python, JS) Linguagens onde os tipos de dados são associados às variáveis em tempo de execução. O tipo de dado de uma variável pode mudar durante a execução do programa.

- Estaticamente tipado: (e.g. C++ ou Java) variáveis recebem tipo explicitamente definido na sua declaração e isso é verificado em tempo de compilação. O tipo é imutável.

### [6] - Garbage collection
Coleta de lixo

- Mecanismo automático utilizado para gerenciar a alocação e desalocação de memória
- Recupera a memória que não está mais sendo utilizada
- Ajuda a evitar vazamentos de memória (memory leaks)
- Simplifica o uso de memória para os desenvolvedores.
    - Usam garbage collection: Java, C#, Python e JavaScript 
    - Não usam garbage collection: C, C++, Rust



## TERMINAL

### comandos

- python3 --version : mostrar a versão do python
- ls : listar arquivos
- python3 : entrar no terminal do python
    - exit() : sair do terminal do python
- nano (nome do arquivo).py : criar arquivo rm python

### arquivo em python
```
felipe = 19
livia = 21
guilherme = 19

media = (felipe + livia + guilherme) / 3

print('a média é', media)
print('a média é' + str(media)
```