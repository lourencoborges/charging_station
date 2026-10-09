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

Na página inicial, a pessoa escolhe entre a área do usuário e a área do ADM. O sistema permite cadastrar sessões, consultar e listar os registros, ordenar por placa e acompanhar estatísticas e um relatório. A lista fica em memória durante a execução; os dados não são salvos em arquivo ou banco de dados.

## Funcionalidades

- **Área do ADM:** mantém cadastro manual de sessões, listagem, busca por placa, ordenação, estatísticas e relatório. O cadastro manual salva imediatamente, sem espera.
- **Sessões aleatórias:** na área do ADM, gera e cadastra uma sessão com placa ainda não usada, energia e duração aleatórias; na área do usuário, gera uma placa livre e os dados de bateria e inicia a recarga simulada.
- **Área do usuário:** registra placa, capacidade da bateria em kWh, porcentagem inteira inicial e porcentagem inteira desejada. A carga simulada avança 3 pontos percentuais por segundo. Ao alcançar o objetivo, fica como concluída; o botão permite finalizar antes da hora; ao sair da página com uma recarga ativa, o sistema tenta registrá-la como incompleta. O tempo é guardado em segundos inteiros.
- **Calcular energia estimada:** usa a capacidade da bateria e a diferença entre a porcentagem final e inicial.
- **Calcular custo e potência:** cada sessão calcula o custo pela tarifa de R$ 0,85 por kWh e a potência média em kW.
- **Listar sessões:** exibe os registros cadastrados e informa quando a lista está vazia.
- **Buscar sessão:** localiza a sessão mais recente da placa informada usando busca sequencial.
- **Ordenar sessões:** organiza a lista por placa crescente usando Bubble Sort implementado no código.
- **Consultar estatísticas e relatório:** apresenta quantidade de sessões, energia total, custo total e médio, maior e menor consumo, além dos dados das sessões.
- **Validar entradas:** trata placas inválidas ou já cadastradas, porcentagens fora do intervalo, capacidade e energia não positivas, duração inválida, entradas não numéricas e buscas sem resultado.

Ao iniciar a aplicação, há três sessões de exemplo já cadastradas. Como os dados são mantidos somente em memória, alterações feitas durante a execução são perdidas quando o servidor é encerrado.

## Estrutura de dados e cálculos

Cada registro é um objeto da classe `Sessao`, definida em `Sprint_Python_Dados/models.py`. Seus atributos incluem:

- `placa`: identificação do veículo;
- `energia`: energia consumida, em kWh;
- `tempo_segundos`: duração medida da recarga em segundos;
- `status`: estado da recarga;
- `bateria_inicial`, `bateria_final` e `capacidade_bateria_kwh`: dados informados pelo usuário;
- `potencia_media_kw`: energia dividida pelo tempo convertido em horas;
- `custo`: energia multiplicada pela tarifa de R$ 0,85 por kWh.

Os objetos são armazenados na lista `sessoes`, em `main.py`. A tarifa está definida na constante `TARIFA_POR_KWH` da classe. A potência média é calculada em kW e os valores de potência e custo são arredondados para duas casas decimais.

## Algoritmos e complexidade

### Busca sequencial

Na busca por placa, o sistema percorre a lista e compara a placa de cada sessão com a informada. No pior caso, visita todos os `n` registros; portanto, sua complexidade de tempo é **O(n)**.

### Bubble Sort

A ordenação compara placas de elementos adjacentes e troca suas posições quando estão fora de ordem. Com dois laços sobre a lista, sua complexidade de tempo é **O(n²)**. O algoritmo está implementado diretamente na rota `/ordenar-sessoes`.

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
        ├── admin.html
        ├── usuario.html
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
| `/admin` | Área do ADM |
| `/usuario` | Área do usuário |
| `/nova-sessao` | Cadastro manual do ADM |
| `/usuario/iniciar` | Início de uma recarga do usuário |
| `/usuario/finalizar/<id>` | Finalização e registro do tempo |
| `/listar-sessoes` | Listagem de sessões |
| `/buscar-sessao` | Busca por placa |
| `/ordenar-sessoes` | Ordenação por placa |
| `/estatisticas` | Estatísticas das sessões |
| `/relatorio` | Resumo e dados das sessões |

## Observações

- A aplicação inicia em modo de depuração (`debug=True`), adequado para desenvolvimento local.
- As sessões ficam em memória e voltam aos valores iniciais a cada reinicialização.
- A capacidade da bateria é solicitada para estimar a energia correspondente à porcentagem carregada.
- As recargas em andamento e as sessões concluídas são mantidas em memória enquanto o servidor está ligado.
