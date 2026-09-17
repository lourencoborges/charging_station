from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)





def main():
    print("""
    =====================================
            ESTAÇÃO DE RECARGA
    =====================================

    1 - Nova sessão de recarga
    2 - Listar sessões
    3 - Buscar sessão
    4 - Ordenar sessões
    5 - Estatísticas
    6 - Encerrar
    """)

    while True:
        try:
            escolha_usuario = int(input("Escolha: "))

            if escolha_usuario >= 7 or escolha_usuario <= 0:
                print("Use um número entre 1 e 6!")
            else:
                return escolha_usuario

        except ValueError:
            print("Bote apenas números!")







class Sessao:
    def __init__(self, id, energia, tempo, custo):
        self.id = id
        self.energia = energia 
        self.tempo = tempo
        self.custo = custo
        
sessoes = [
    Sessao(2, 50, 60, 30),
    Sessao(1, 70, 80, 40),
    Sessao(3, 40, 20, 50)
]

    

def cadastrar_sessao():
    print()
    while True:
        try:
            id = int(input("Digite o ID: "))
            if id > 0:
                id_existe = False
                
                for sessao in sessoes:
                    if id == sessao.id:
                        id_existe = True
                        print("Esse Id ja existe")
            
                if id_existe:
                    continue
                break
            else:
                print("Digite um valor positivo")
        except ValueError:
            print("Digite um numero")
            
        
    while True:
        try:
            energia = float(input("Digite a energia: "))
            if energia > 0:
                break
            else:
                print("A energia deve ser maior que zero")
        
        except ValueError:
            print("Digite um numero para a energia")
    
    while True:
        try:
            tempo = int(input("Digite o tempo: "))
            if tempo > 0:
                break
            else:
                print("Digite um valor maior que 0")
        except ValueError:
            print("Digite numeros no tempo")
    
    while True:
        try:
            custo = float(input("Digite o custo: "))
            if custo > 0:
                break
                
            else:
                print("Digite um valor maior que zero")
        except ValueError:
            print("Digite um numero")
    print()
    input("Clique no Enter para sair")
    
    
    sessoes.append(Sessao(id, energia, tempo, custo))









def listar_sessoes():
    print()
    print("==================")
    print("      LISTA       ")
    print("==================")
    print()
    for sessao in sessoes:
        print("ID: ", sessao.id)
        print("Energia: ", sessao.energia)
        print("Tempo: ", sessao.tempo)
        print("Custo: ", sessao.custo)
        print("")
    input("Clique no Enter para sair")
        





def buscar_sessao():
    print()
    while True:
        try:
            id_busca = int(input("Digite o ID em que voce quer encontrar: "))
            if id_busca > 0:
                encontrou = False
                for sessao in sessoes:
                    if sessao.id == id_busca:
                        encontrou = True
                        print("==================")
                        print("  SASSÃO BUSCADA  ")
                        print("==================")
                        print("ID:", sessao.id)
                        print("Energia:", sessao.energia)
                        print("Tempo:", sessao.tempo)
                        print("Custo:", sessao.custo)
                        break
                if encontrou:
                    break
                else:
                    print("ID nao encontrado")
            else:
                print("Digite um ID positivo")
        except ValueError:
            print("Digite um ID")
    print()
    input("Clique no Enter para sair")






def ordenar_sessoes():
    for i in range(len(sessoes)):
        for sessao in range(len(sessoes) - 1):
            if sessoes[sessao].id > sessoes[sessao + 1].id:
                sessoes[sessao], sessoes[sessao + 1] = sessoes[sessao + 1], sessoes[sessao]
    print()
    print("Sessões ordenadas com sucesso")
    print()
    input("Clique no Enter para sair")



    #esse codigo consegue ve o total de energia que a lsita(sessoes) tem,
    #quanto de dinheiro tem na lista,
    #maior consumo e
    #menor consumo
def mostrar_estatisticas():

    #conta quantas sessoes tem
    contagem_sessao = len(sessoes)
    total_receita = 0
    total_energia = 0

    #verifica se existe receita ou uma lista para não ocorrer uma divisão por 0
    if contagem_sessao == 0:
        print("Erro, não existe uma sessão")
        return
    maior_consumo = sessoes[0].energia
    menor_consumo = sessoes[0].energia

    #passa por toda a lista e vai colocando o total de energia e o total de receita
    for sessao in sessoes:
        total_energia += sessao.energia
        total_receita += sessao.custo

        #esse codigo ve o maior e o menor consumo de energia
        if sessao.energia > maior_consumo:
            maior_consumo = sessao.energia
        if menor_consumo > sessao.energia:
            menor_consumo = sessao.energia
    
    #esse vai calcular o custo medio das sessoes
    custo_medio = total_receita / contagem_sessao
    print()
    print("========================================")
    print("         ESTATISTÍCAS                   ")
    print("========================================")
    print("Sessões existentes:", contagem_sessao)
    print("Total de energia: ", total_energia)
    print("Receita total: ", total_receita)
    print("O custo medio: ", round(custo_medio, 2))
    print("O maior consumo: ", maior_consumo)
    print("O menor consumo: ", menor_consumo)
    print()
    input("Clique no Enter para sair")
    


#menu principal
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
        