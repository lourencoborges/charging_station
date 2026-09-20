from flask import Flask, render_template, request, flash





#apenas o python, a web esta no final da pagina
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
    


#menu principal da web
app = Flask(__name__)

app.secret_key = "chave-secreta"


@app.route("/")
def inicio():
    return render_template("index.html")



@app.route("/nova-sessao", methods=["GET", "POST"])
def nova_sessao():
    if request.method == "POST":
        try:
            id = int(request.form["id"])

            if id <= 0:
                flash("O ID deve ser maior que zero.")
                return render_template("nova_sessao.html")
        except ValueError:
            flash("Digite um ID válido.")
            return render_template("nova_sessao.html")
        
        for sessao in sessoes:
            if id == sessao.id:
                flash("Esse ID já existe.")
                return render_template("nova_sessao.html")


        try:
            energia = float(request.form["energia"])
            if energia <= 0:
                flash("A energia deve ser maior que zero.")
                return render_template("nova_sessao.html")
        except ValueError:
            flash("Digite uma energia válida.")
            return render_template("nova_sessao.html")


        try:
            tempo = int(request.form["tempo"])
            if tempo <= 0:
                flash("O tempo deve ser maior que zero")
                return render_template("nova_sessao.html")
        except ValueError:
            flash("Digite um tempo válido")
            return render_template("nova_sessao.html")


        try:
            custo = float(request.form["custo"])
            if custo <= 0:
                flash("O custo deve ser maior que zero.")
                return render_template("nova_sessao.html")
        except ValueError:
            flash("Digite um custo válido")
            return render_template("nova_sessao.html")


        sessoes.append(Sessao(id, energia, tempo, custo))
        flash("Sessão cadastrada com sucesso!")
    return render_template("nova_sessao.html")



@app.route("/listar-sessoes")
def listar_sessoes_web():
    if len(sessoes) == 0:
        mensagem = "Nenhuma sessão cadastrada."
    else:
        mensagem = ""

    return render_template("listar_sessoes.html", sessoes=sessoes, mensagem=mensagem)


@app.route("/buscar-sessao", methods=["GET", "POST"])
def buscar_sessao_web():
    if request.method == "POST":
        try:
            id_busca = int(request.form["id"])
        except ValueError:
            flash("Digite um ID válido.")
            return render_template("buscar_sessao.html")

        encontrou=False
        for sessao in sessoes:
            if sessao.id == id_busca:
                encontrou=True
                return render_template("buscar_sessao.html", sessao=sessao)

        if not encontrou:
            flash("ID não encontrado.")
            return render_template("buscar_sessao.html")

    return render_template("buscar_sessao.html")


@app.route("/ordenar-sessoes", methods=["GET", "POST"])
def ordenar_sessoes_web():

    if request.method == "POST":
        n = len(sessoes)

        for i in range(n):
            for j in range(0, n - i - 1):

                if sessoes[j].id > sessoes[j + 1].id:
                    sessoes[j], sessoes[j + 1] = sessoes[j + 1], sessoes[j]

        flash("Ordenação completa")
        return render_template("ordenar_sessoes.html")

    return render_template("ordenar_sessoes.html")


@app.route("/estatisticas")
def estatisticas_web():

    total_sessoes = len(sessoes)
    total_energia = 0
    custo_total = 0
    custo_medio = 0
    maior_consumo = sessoes[0].energia
    menor_consumo = sessoes[0].energia


    for sessao in sessoes:
        if sessao.energia > maior_consumo:
            maior_consumo = sessao.energia
        elif menor_consumo > sessao.energia:
            menor_consumo = sessao.energia


    for sessao in sessoes:
        total_energia += sessao.energia
        custo_total += sessao.custo


    if total_sessoes == 0:
            mensagem = "Nenhuma sessão cadastrada."
    else:
        mensagem = ""
        custo_medio = custo_total / total_sessoes


    

    return render_template("estatisticas.html",
                            sessoes=sessoes,
                            mensagem=mensagem,
                              total_energia=total_energia,
                              custo_total=custo_total,
                              custo_medio=custo_medio,
                              maior_consumo=maior_consumo,
                              menor_consumo=menor_consumo)



if __name__ == "__main__":
    app.run(debug=True)