from flask import Flask, render_template, request, flash


#a classe para podemos criar varias sessoes como mostra o codigo abaixo
class Sessao:
    def __init__(self, id, energia, tempo, custo):
        self.id = id
        self.energia = energia 
        self.tempo = tempo
        self.custo = custo


#uma lista(sessoes) que dentro tem a classe Sessao
sessoes = [
    Sessao(2, 50, 60, 30),
    Sessao(1, 70, 80, 40),
    Sessao(3, 40, 20, 50)
]

#menu principal da web
app = Flask(__name__)

#essa linha de codigo deixa ultilizar o flash()
app.secret_key = "chave-secreta"


#deixa eu abrir o index.html
@app.route("/")
def inicio():
    return render_template("index.html")


#deixa eu abrir o nova_sessao.html, onde eu posso adicionar as novas sessões
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


#deixa abrir a lsita
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


#codigo que ordena a lista(sessoes)
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


#deixa ver a estatistica da lista(sessoes)
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


#inicia um servidor local
if __name__ == "__main__":
    app.run(debug=True)