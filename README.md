# Sistema de Gerenciamento de Estação de Recarga

### Integrantes:
<p>
Lourenço Borges da Silva — RM 569515<br>
Gustavo Curis de Francisco — RM 569704<br>
Caio César Portela França — RM 573127<br>
Tiago Pimentel Muniz — RM 574148<br>
Davi Teodoro Novais — RM 571022
</p>

## Sobre o projeto

Este projeto é uma aplicação web para simular e acompanhar sessões de recarga de veículos elétricos. Ele foi desenvolvido em Python como parte da Sprint de Estruturas de Dados, com uma interface feita em Flask, HTML e CSS.

O sistema permite cadastrar sessões, consultar e listar os registros, ordenar por ID e acompanhar estatísticas e um relatório. A lista de sessões fica em memória durante a execução da aplicação; os dados não são salvos em arquivo ou banco de dados.

## Funcionalidades

- **Cadastrar sessão:** recebe ID, energia consumida em kWh e duração em minutos. O ID deve ser positivo e único; energia e duração também devem ser maiores que zero.
- **Calcular custo e potência:** cada sessão calcula o custo pela tarifa de R$ 0,85 por kWh e a potência média em kW.
- **Simular recarga:** novas sessões começam com o status “Em andamento” e passam para “Concluida” após cinco segundos.
- **Listar sessões:** exibe os registros cadastrados e informa quando a lista está vazia.
- **Buscar sessão:** localiza um registro pelo ID usando busca sequencial.
- **Ordenar sessões:** organiza a lista por ID crescente usando Bubble Sort implementado no código.
- **Consultar estatísticas e relatório:** apresenta quantidade de sessões, energia total, custo total e médio, maior e menor consumo, além dos dados das sessões.
- **Validar entradas:** trata valores inválidos, IDs repetidos e buscas sem resultado.

Ao iniciar a aplicação, há três sessões de exemplo já cadastradas. Como os dados são mantidos somente em memória, alterações feitas durante a execução são perdidas quando o servidor é encerrado.

## Estrutura de dados e cálculos

Cada registro é um objeto da classe `Sessao`, definida em `Sprint_Python_Dados/models.py`. Seus atributos incluem:

- `id`: identificador da sessão;
- `energia`: energia consumida, em kWh;
- `tempo`: duração, em minutos;
- `status`: estado da recarga;
- `potencia_media_kw`: energia dividida pelo tempo convertido em horas;
- `custo`: energia multiplicada pela tarifa de R$ 0,85 por kWh.

Os objetos são armazenados na lista `sessoes`, em `main.py`. A tarifa está definida na constante `TARIFA_POR_KWH` da classe. A potência média é calculada em kW e os valores de potência e custo são arredondados para duas casas decimais.

## Algoritmos e complexidade

### Busca sequencial

Na busca por ID, o sistema percorre a lista e compara o identificador de cada sessão com o informado. No pior caso, visita todos os `n` registros; portanto, sua complexidade de tempo é **O(n)**.

### Bubble Sort

A ordenação compara elementos adjacentes e troca suas posições quando estão fora de ordem. Com dois laços sobre a lista, sua complexidade de tempo é **O(n²)**. O algoritmo está implementado diretamente na rota `/ordenar-sessoes`.

## Tecnologias

- Python 3
- Flask
- HTML
- CSS

## Estrutura do projeto

```text
charging_station/
├── README.md
└── Sprint_Python_Dados/
    ├── main.py
    ├── models.py
    ├── assets/
    │   └── EV Charging Infrastructure Growth, Challenges & Future Trend.jpeg
    ├── static/
    │   └── style.css
    └── templates/
        ├── index.html
        ├── nova_sessao.html
        ├── listar_sessoes.html
        ├── buscar_sessao.html
        ├── ordenar_sessoes.html
        ├── estatisticas.html
        └── relatorio.html
```

## Como executar

É necessário ter Python 3 instalado. No terminal, a partir da pasta raiz do projeto, instale as dependências e inicie a aplicação:

```bash
python -m pip install -r requirements.txt
cd Sprint_Python_Dados
python main.py
```

O arquivo `requirements.txt` lista as dependências externas necessárias para executar o projeto.

Abra no navegador o endereço local mostrado no terminal, normalmente `http://127.0.0.1:5000/`.

## Rotas disponíveis

| Rota | Uso |
| --- | --- |
| `/` | Página inicial |
| `/nova-sessao` | Cadastro de sessão |
| `/listar-sessoes` | Listagem de sessões |
| `/buscar-sessao` | Busca por ID |
| `/ordenar-sessoes` | Ordenação por ID |
| `/estatisticas` | Estatísticas das sessões |
| `/relatorio` | Resumo e dados das sessões |

## Observações

- A aplicação inicia em modo de depuração (`debug=True`), adequado para desenvolvimento local.
- As sessões ficam em memória e voltam aos valores iniciais a cada reinicialização.
- A simulação altera o status da sessão em uma thread após cinco segundos.
