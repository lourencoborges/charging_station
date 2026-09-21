# Estruturas de Dados e Evolução do Simulador de Recarga em Python


### Integrantes:
<p>
Lourenço Borges da Silva — RM 569515<br>
Gustavo Curis de Francisco — RM 569704<br>
Caio César Portela França — RM 573127<br>
Tiago Pimentel Muniz — RM 574148<br>
Davi Teodoro Novais — RM 571022
</p>

## 1. Sobre o projeto

Este projeto é a evolução do simulador de sessões de recarga desenvolvido nas etapas anteriores. Nesta Sprint, o simulador deixou de trabalhar apenas com uma única recarga e passou a funcionar como um pequeno **Sistema de Gerenciamento de Estação de Recarga**.

A proposta foi aplicar, em um sistema funcional, os conteúdos de **classes, objetos, listas, funções, busca, ordenação, algoritmos e análise de complexidade (Big-O)**.

Além da versão baseada na lógica em Python, o projeto foi evoluído para uma **interface web utilizando Flask, HTML e CSS**, permitindo que as operações do sistema sejam realizadas por meio de páginas no navegador.

> A interface web é uma evolução da forma de utilização do sistema. As estruturas de dados e os algoritmos exigidos na Sprint continuam sendo implementados em Python, sem substituir a busca e a ordenação por recursos prontos da linguagem.

---

## 2. Objetivo da Sprint

O objetivo da Sprint é transformar o simulador em um sistema capaz de **registrar, armazenar, organizar, pesquisar e analisar múltiplas sessões de recarga**.

O projeto foi desenvolvido mantendo os critérios definidos no enunciado:

- representação adequada de uma sessão;
- armazenamento de múltiplas sessões em uma lista;
- funções para organização do programa;
- busca implementada explicitamente;
- ordenação implementada manualmente;
- menu funcional;
- estatísticas;
- tratamento de entradas inválidas;
- análise de complexidade dos algoritmos utilizados.

---

## 3. Estrutura de dados

Cada sessão de recarga é representada por uma classe `Sessao`.

```python
class Sessao:
    def __init__(self, id, energia, tempo, custo):
        self.id = id
        self.energia = energia
        self.tempo = tempo
        self.custo = custo
```

A classe possui quatro informações principais:

- `id`: identificação da sessão;
- `energia`: quantidade de energia da recarga;
- `tempo`: tempo da recarga;
- `custo`: custo da sessão.

As sessões são armazenadas em uma lista:

```python
sessoes = []
```

Cada novo objeto `Sessao` é inserido nessa lista. Dessa forma, o sistema consegue trabalhar com várias sessões ao mesmo tempo.

A quantidade de sessões armazenadas é obtida por:

```python
len(sessoes)
```

---

## 4. Evolução para aplicação web

Uma das evoluções realizadas no projeto foi transformar a interação do programa em uma aplicação web utilizando **Flask**.

Com isso, as funcionalidades da Sprint passaram a ser acessadas por páginas no navegador.

A aplicação possui páginas para:

- cadastrar uma nova sessão;
- listar as sessões;
- buscar uma sessão;
- ordenar as sessões;
- visualizar as estatísticas.

A interface foi construída com **HTML** e estilizada com **CSS**.

O Flask é responsável por receber as requisições, executar a lógica em Python e enviar os dados para os templates HTML.

### Rotas principais

```text
/
├── /nova-sessao
├── /listar-sessoes
├── /buscar-sessao
├── /ordenar-sessoes
└── /estatisticas
```

Essa evolução mantém a lógica solicitada pelo professor e acrescenta uma forma mais completa de interação com o sistema.

---

## 5. Funcionalidades

### 5.1 Nova sessão de recarga

A página de cadastro permite informar:

- ID;
- energia;
- tempo;
- custo.

Antes de cadastrar a sessão, o sistema realiza validações.

São impedidos:

- IDs menores ou iguais a zero;
- IDs duplicados;
- energia menor ou igual a zero;
- tempo menor ou igual a zero;
- custo menor ou igual a zero;
- entradas que não correspondem ao tipo esperado.

As mensagens de erro são apresentadas ao usuário por meio do sistema de mensagens do Flask.

---

### 5.2 Listar sessões

A funcionalidade de listagem percorre a lista `sessoes` e apresenta as informações cadastradas.

Para cada sessão são exibidos:

- ID;
- energia;
- tempo;
- custo.

Também é possível identificar a quantidade de sessões armazenadas.

Quando não existem sessões cadastradas, o sistema apresenta uma mensagem informando essa situação.

---

### 5.3 Buscar sessão

A busca é realizada pelo ID da sessão.

Foi utilizado o algoritmo de **Busca Sequencial**, implementado diretamente no código:

```python
for sessao in sessoes:
    if sessao.id == id_busca:
        # sessão encontrada
```

O sistema percorre as sessões uma por uma até encontrar o ID procurado.

Quando a sessão é encontrada, seus dados são apresentados. Caso contrário, o usuário recebe a mensagem de que o ID não foi encontrado.

A busca foi implementada explicitamente, conforme solicitado no enunciado, sem utilizar uma função pronta para substituir o algoritmo.

---

## 6. Ordenação

As sessões são ordenadas pelo ID em ordem crescente.

Foi implementado manualmente o algoritmo **Bubble Sort**.

A lógica compara elementos vizinhos e troca suas posições quando estão na ordem incorreta:

```python
if sessoes[j].id > sessoes[j + 1].id:
    sessoes[j], sessoes[j + 1] = sessoes[j + 1], sessoes[j]
```

A estrutura utilizada no projeto é:

```python
n = len(sessoes)

for i in range(n):
    for j in range(0, n - i - 1):
        if sessoes[j].id > sessoes[j + 1].id:
            sessoes[j], sessoes[j + 1] = sessoes[j + 1], sessoes[j]
```

Não foram utilizados:

```python
sessoes.sort()
```

ou:

```python
sorted(sessoes)
```

Isso mantém a implementação de ordenação de acordo com a restrição estabelecida no enunciado.

---

## 7. Estatísticas

A aplicação calcula estatísticas utilizando os dados armazenados nas sessões.

São calculados:

- quantidade total de sessões;
- energia total;
- faturamento total;
- custo médio por sessão;
- maior consumo;
- menor consumo.

Os cálculos são realizados percorrendo a lista de sessões e acumulando os valores necessários.

O custo médio é calculado pela relação:

```python
custo_medio = custo_total / total_sessoes
```

Quando não existem sessões cadastradas, o sistema informa essa situação em vez de apresentar dados incorretos.

---

## 8. Organização do programa

O projeto foi dividido em funções e rotas responsáveis por diferentes operações.

Entre as principais funcionalidades estão:

- cadastro de sessões;
- listagem;
- busca;
- ordenação;
- estatísticas;
- validação de entradas.

Essa divisão evita concentrar toda a lógica em um único bloco e facilita a manutenção do sistema.

---

## 9. Tratamento de entradas inválidas

O sistema possui tratamento para diferentes situações de entrada inválida.

São tratados casos como:

- valores não numéricos;
- valores negativos;
- valores iguais a zero quando não permitidos;
- IDs duplicados;
- IDs inexistentes durante uma busca;
- ausência de sessões cadastradas.

Na aplicação web, erros de conversão dos valores recebidos dos formulários são tratados com `try`/`except`, evitando que uma entrada incorreta encerre a aplicação.

Mensagens são apresentadas ao usuário para indicar o problema e orientar a correção.

---

## 10. Análise de complexidade — Big-O

A Sprint solicita a análise da complexidade de dois algoritmos utilizados no próprio projeto.

### 10.1 Busca Sequencial — O(n)

A Busca Sequencial possui complexidade **O(n)** no pior caso.

Isso acontece porque o algoritmo percorre a lista de sessões uma posição por vez:

```python
for sessao in sessoes:
    if sessao.id == id_busca:
        ...
```

Considerando `n` sessões:

- se a sessão estiver no início, poucas comparações podem ser necessárias;
- se estiver no final, todas as sessões podem ser verificadas;
- se não existir, todas as sessões serão verificadas.

Portanto, no pior caso, são realizadas aproximadamente `n` verificações, resultando em **O(n)**.

### 10.2 Bubble Sort — O(n²)

O Bubble Sort utilizado no projeto possui complexidade **O(n²)** no pior caso.

Isso ocorre devido aos dois laços de repetição:

```python
for i in range(n):
    for j in range(0, n - i - 1):
```

O primeiro laço controla as passagens pela lista e o segundo realiza as comparações entre os elementos.

Conforme a quantidade `n` de sessões aumenta, a quantidade de comparações cresce aproximadamente de forma quadrática.

Por isso, a complexidade é **O(n²)**.

---

## 11. Relação entre os algoritmos e os dados

Os algoritmos foram escolhidos e implementados considerando a estrutura utilizada no projeto.

A lista `sessoes` armazena os objetos `Sessao`, e tanto a busca quanto a ordenação acessam o atributo `id` de cada objeto.

Assim:

```text
Lista de sessões
       ↓
Objetos Sessao
       ↓
Acesso ao atributo id
       ↓
Busca Sequencial / Bubble Sort
       ↓
Resultados apresentados na aplicação web
```

Essa integração demonstra a relação entre a estrutura de dados, os algoritmos e o funcionamento do sistema.

---

## 12. Tecnologias utilizadas

- **Python** — lógica, estruturas de dados e algoritmos;
- **Flask** — desenvolvimento da aplicação web e criação das rotas;
- **HTML** — estrutura das páginas;
- **CSS** — estilização da interface.

---

## 13. Estrutura do projeto

A organização utilizada no projeto é composta pela aplicação Python, pelos templates HTML e pelos arquivos de estilo.

```text
charging_station/
│
├── main.py
├── README.md
│
└── Sprint_Python_Dados/
    │
    ├── templates/
    │   ├── index.html
    │   ├── nova_sessao.html
    │   ├── listar_sessoes.html
    │   ├── buscar_sessao.html
    │   ├── ordenar_sessoes.html
    │   └── estatisticas.html
    │
    └── static/
        └── style.css
```

---

## 14. Como executar

Com o Python instalado e o ambiente do projeto configurado, execute a aplicação Flask pelo arquivo responsável pela inicialização do projeto.

Após iniciar o servidor, acesse a aplicação pelo endereço local informado pelo Flask no terminal.

A partir da página inicial, o usuário pode acessar as funcionalidades de cadastro, listagem, busca, ordenação e estatísticas.

---

## 15. Resultado do projeto

O resultado desta Sprint é um sistema que evolui o simulador inicial para um pequeno **Sistema de Gerenciamento de Estação de Recarga**.

O projeto demonstra a integração entre:

```text
Estrutura de dados
        ↓
Lista de sessões
        ↓
Funções e rotas
        ↓
Busca
        ↓
Ordenação
        ↓
Estatísticas
        ↓
Interface web
        ↓
Análise de complexidade
```

A implementação mantém os conteúdos algorítmicos solicitados na Sprint e utiliza a interface web como uma evolução da apresentação e da interação com o sistema.

O desenvolvimento também demonstra, na prática, como uma mesma estrutura de dados pode ser utilizada para realizar cadastro, consulta, organização e análise das informações de múltiplas sessões de recarga.
