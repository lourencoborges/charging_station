# Estação de Recarga

Sistema desenvolvido em Python para gerenciamento de sessões de recarga de veículos elétricos.

O projeto permite cadastrar, listar, buscar, ordenar e analisar sessões de recarga por meio de um menu interativo no terminal.

## Objetivo

O objetivo do projeto é evoluir um simulador de recarga para um sistema capaz de armazenar e gerenciar múltiplas sessões.

O sistema utiliza estruturas de dados, programação orientada a objetos, algoritmos de busca e ordenação, além de validações para evitar entradas inválidas.

---

## Tecnologias utilizadas

* **Python**
* Programação Orientada a Objetos
* Listas
* Estruturas de repetição
* Estruturas condicionais
* Busca Sequencial
* Bubble Sort
* Tratamento de exceções

---

## Estrutura dos dados

As sessões são representadas através da classe `Sessao`.

```python
class Sessao:
    def __init__(self, id, energia, tempo, custo):
        self.id = id
        self.energia = energia
        self.tempo = tempo
        self.custo = custo
```

Cada sessão possui quatro informações:

| Atributo  | Descrição                       |
| --------- | ------------------------------- |
| `id`      | Identificador da sessão         |
| `energia` | Quantidade de energia utilizada |
| `tempo`   | Tempo da sessão                 |
| `custo`   | Custo da recarga                |

As sessões são armazenadas em uma lista:

```python
sessoes = []
```

Novas sessões são adicionadas utilizando:

```python
sessoes.append(Sessao(id, energia, tempo, custo))
```

---

## Funcionalidades

O sistema possui um menu com as seguintes opções:

```text
=====================================
        ESTAÇÃO DE RECARGA
=====================================

1 - Nova sessão de recarga
2 - Listar sessões
3 - Buscar sessão
4 - Ordenar sessões
5 - Estatísticas
6 - Encerrar
```

### 1. Nova sessão de recarga

Permite cadastrar uma nova sessão.

Durante o cadastro, o sistema verifica:

* Se o ID é um número válido;
* Se o ID é positivo;
* Se o ID já está cadastrado;
* Se a energia é maior que zero;
* Se o tempo é maior que zero;
* Se o custo é maior que zero;
* Se os valores digitados possuem o tipo correto.

O sistema utiliza `try` e `except ValueError` para evitar que entradas incompatíveis encerrem o programa.

---

### 2. Listar sessões

Percorre a lista `sessoes` e apresenta os dados de cada sessão cadastrada:

* ID;
* Energia;
* Tempo;
* Custo.

A listagem utiliza um laço `for` para acessar cada objeto `Sessao` armazenado na lista.

---

### 3. Buscar sessão

A busca é realizada através de uma **Busca Sequencial**.

O usuário informa o ID que deseja encontrar e o programa percorre as sessões uma por uma até encontrar uma sessão com o ID correspondente.

Exemplo:

```python
for sessao in sessoes:
    if sessao.id == id_busca:
        ...
        break
```

Quando a sessão é encontrada, o `break` encerra a busca.

Caso o ID não exista, o sistema informa que a sessão não foi encontrada.

#### Complexidade

A Busca Sequencial possui complexidade:

**O(n)**

Isso acontece porque, no pior caso, pode ser necessário verificar todos os elementos da lista.

---

### 4. Ordenar sessões

As sessões são ordenadas pelo ID utilizando o algoritmo **Bubble Sort**, implementado manualmente.

O algoritmo compara sessões vizinhas:

```python
if sessoes[sessao].id > sessoes[sessao + 1].id:
    sessoes[sessao], sessoes[sessao + 1] = \
    sessoes[sessao + 1], sessoes[sessao]
```

Quando o ID da sessão atual é maior que o ID da próxima sessão, os objetos são trocados de posição.

O programa não utiliza `sort()` ou `sorted()` para realizar a ordenação.

#### Complexidade

O Bubble Sort possui complexidade:

**O(n²)**

Isso ocorre porque o algoritmo utiliza dois laços de repetição aninhados para realizar as comparações.

---

### 5. Estatísticas

A opção de estatísticas apresenta informações sobre as sessões cadastradas:

* Quantidade total de sessões;
* Total de energia;
* Receita total;
* Custo médio por sessão;
* Maior consumo de energia;
* Menor consumo de energia.

#### Total de sessões

A quantidade de sessões é obtida utilizando:

```python
len(sessoes)
```

#### Total de energia

O sistema percorre todas as sessões e soma o valor de energia:

```python
total_energia = 0

for sessao in sessoes:
    total_energia += sessao.energia
```

#### Receita total

O custo de cada sessão é acumulado:

```python
total_receita = 0

for sessao in sessoes:
    total_receita += sessao.custo
```

#### Custo médio

O custo médio é calculado dividindo a receita total pela quantidade de sessões:

```python
custo_medio = total_receita / contagem_sessao
```

O resultado é apresentado com duas casas decimais.

#### Maior consumo

O maior consumo começa utilizando a energia da primeira sessão como referência:

```python
maior_consumo = sessoes[0].energia
```

Depois, cada sessão é comparada com o maior valor encontrado.

#### Menor consumo

O menor consumo utiliza a mesma lógica:

```python
menor_consumo = sessoes[0].energia
```

Cada sessão é comparada com o menor valor encontrado até então.

O programa também verifica se existem sessões antes de acessar `sessoes[0]`, evitando erros quando a lista está vazia.

---

## Validações

O sistema possui tratamento para diferentes situações de entrada inválida.

Entre elas:

* IDs duplicados;
* IDs menores ou iguais a zero;
* Energia menor ou igual a zero;
* Tempo menor ou igual a zero;
* Custo menor ou igual a zero;
* Entrada de letras onde são esperados números;
* Busca por ID inexistente;
* Tentativa de calcular estatísticas sem sessões cadastradas.

O tratamento de entradas incompatíveis utiliza:

```python
try:
    ...
except ValueError:
    ...
```

---

## Funcionamento do menu

O programa utiliza um `while True` para manter o sistema funcionando até que o usuário escolha a opção `6`.

A estrutura principal é baseada na escolha do usuário:

```python
while True:

    escolha = main()

    if escolha == 1:
        cadastrar_sessao()

    elif escolha == 2:
        listar_sessoes()

    elif escolha == 3:
        buscar_sessao()

    elif escolha == 4:
        ordenar_sessoes()

    elif escolha == 5:
        mostrar_estatisticas()

    elif escolha == 6:
        break
```

Após executar uma operação, o programa retorna ao menu principal.

Para facilitar a navegação, as operações podem utilizar `input()` para aguardar o usuário antes de retornar ao menu.

---

## Conceitos praticados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

* Classes e objetos;
* Atributos;
* `self`;
* Listas;
* `append()`;
* `len()`;
* `for`;
* `while`;
* `if`, `elif` e `else`;
* `break`;
* `continue`;
* `return`;
* `try` e `except`;
* Busca Sequencial;
* Bubble Sort;
* Acumuladores;
* Comparação de valores;
* Complexidade de algoritmos com Big-O.

---

## Complexidade dos algoritmos

| Algoritmo        | Complexidade |
| ---------------- | ------------ |
| Busca Sequencial | **O(n)**     |
| Bubble Sort      | **O(n²)**    |

### Busca Sequencial — O(n)

No pior caso, o algoritmo precisa percorrer todos os elementos da lista para encontrar o ID procurado ou confirmar que ele não existe.

### Bubble Sort — O(n²)

O algoritmo utiliza dois laços de repetição para realizar diversas comparações entre os elementos da lista. Por isso, conforme a quantidade de sessões aumenta, o número de operações cresce aproximadamente de forma quadrática.

---

## Como executar

É necessário ter o Python instalado.

Execute o arquivo principal do projeto pelo terminal:

```bash
python nome_do_arquivo.py
```

Depois, utilize o menu apresentado no terminal para acessar as funcionalidades do sistema.

---

## Conclusão

O projeto implementa um sistema de gerenciamento de sessões de recarga utilizando Python.

A aplicação trabalha com uma lista de objetos `Sessao` e possui funcionalidades para cadastro, visualização, busca, ordenação e geração de estatísticas.

Além da implementação das funcionalidades, o projeto aplica conceitos de estruturas de dados, programação orientada a objetos, validação de entradas e análise de complexidade de algoritmos.
