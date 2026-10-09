from flask import Flask, flash, jsonify, redirect, render_template, request, send_from_directory, url_for
from pathlib import Path
import math
import random
import re
import string
import threading
import time

from models import Sessao


app = Flask(__name__)
app.secret_key = "chave-secreta"

sessoes = [
    Sessao("ABC1D23", 50, 3600, bateria_inicial=20, bateria_final=80, capacidade_bateria_kwh=83),
    Sessao("DEF4G56", 70, 4800, bateria_inicial=10, bateria_final=90, capacidade_bateria_kwh=87),
    Sessao("GHI7J89", 40, 1200, bateria_inicial=30, bateria_final=70, capacidade_bateria_kwh=67),
]
for numero, sessao in enumerate(sessoes, start=1):
    sessao.id = numero

proximo_id = len(sessoes) + 1
recargas_ativas = {}
sessoes_lock = threading.Lock()


def validar_placa(placa):
    placa = placa.strip().upper()
    if not placa:
        return placa, "Informe a placa do veículo."
    if not re.fullmatch(r"[A-Z0-9]{7}", placa):
        return placa, "A placa deve ter exatamente 7 letras ou números."
    return placa, ""


def placa_ja_cadastrada(placa):
    sessao_concluida = any(sessao.placa == placa for sessao in sessoes)
    recarga_ativa = any(sessao.placa == placa for sessao in recargas_ativas.values())
    return sessao_concluida or recarga_ativa


def gerar_placa_unica():
    caracteres = string.ascii_uppercase + string.digits
    for _ in range(1000):
        placa = "".join(random.choices(caracteres, k=7))
        if not placa_ja_cadastrada(placa):
            return placa
    return None


def resposta_com_erros(erros):
    mensagens = [mensagem for mensagem in erros.values() if mensagem]
    return jsonify({"erro": mensagens[0] if mensagens else "Verifique os dados informados.", "erros": erros}), 400


def criar_sessao(placa, energia, tempo_segundos, **detalhes):
    global proximo_id
    sessao = Sessao(placa, energia, tempo_segundos, **detalhes)
    sessao.id = proximo_id
    proximo_id += 1
    return sessao


@app.route("/assets/background.jpeg")
def imagem_fundo():
    caminho_assets = Path(app.root_path) / "assets"
    return send_from_directory(
        caminho_assets,
        "EV Charging Infrastructure Growth, Challenges & Future Trend.jpeg",
    )


def obter_estatisticas():
    total_energia = sum(sessao.energia for sessao in sessoes)
    custo_total = sum(sessao.custo for sessao in sessoes)
    consumos = [sessao.energia for sessao in sessoes]
    total_sessoes = len(sessoes)
    return {
        "mensagem": "" if total_sessoes else "Nenhuma sessão cadastrada.",
        "total_sessoes": total_sessoes,
        "total_energia": total_energia,
        "custo_total": custo_total,
        "custo_medio": custo_total / total_sessoes if total_sessoes else 0,
        "maior_consumo": max(consumos, default=0),
        "menor_consumo": min(consumos, default=0),
    }


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/admin")
def area_admin():
    return render_template("admin.html")


@app.route("/usuario")
def area_usuario():
    return render_template("usuario.html")


@app.route("/nova-sessao", methods=["GET", "POST"])
def nova_sessao():
    if request.method == "POST":
        if request.form.get("acao") == "aleatoria":
            with sessoes_lock:
                placa = gerar_placa_unica()
                if placa is None:
                    flash("Não foi possível gerar uma placa livre. Tente novamente.")
                    return redirect(url_for("nova_sessao"))
                energia = round(random.uniform(5, 80), 2)
                tempo = random.randint(10, 180)
                sessoes.append(criar_sessao(placa, energia, tempo * 60, status="Concluída"))
            flash(f"Sessão aleatória cadastrada: placa {placa}, {energia} kWh e {tempo} minutos.")
            return redirect(url_for("nova_sessao"))

        erros = {}
        placa, erro_placa = validar_placa(request.form.get("placa", ""))
        erros["placa"] = erro_placa
        try:
            energia = float(request.form.get("energia", ""))
            if not math.isfinite(energia) or energia <= 0:
                raise ValueError
        except (TypeError, ValueError):
            energia = 0
            erros["energia"] = "Informe uma energia válida maior que zero."

        try:
            tempo = int(request.form.get("tempo", ""))
            if tempo <= 0:
                raise ValueError
        except (TypeError, ValueError):
            tempo = 0
            erros["tempo"] = "Informe um tempo inteiro maior que zero."

        if any(erros.values()):
            flash(" ".join(mensagem for mensagem in erros.values() if mensagem))
            return render_template("nova_sessao.html")

        with sessoes_lock:
            if placa_ja_cadastrada(placa):
                flash("Já existe uma sessão cadastrada para essa placa.")
                return render_template("nova_sessao.html")
            sessoes.append(criar_sessao(placa, energia, tempo * 60, status="Concluída"))
        flash("Sessão cadastrada na lista.")
        return redirect(url_for("nova_sessao"))

    return render_template("nova_sessao.html")


@app.route("/usuario/iniciar", methods=["POST"])
def iniciar_recarga_usuario():
    erros = {}
    placa, erro_placa = validar_placa(request.form.get("placa", ""))
    erros["placa"] = erro_placa
    if placa and not erro_placa and placa_ja_cadastrada(placa):
        erros["placa"] = "Já existe uma sessão cadastrada para essa placa."

    try:
        inicial = int(request.form.get("bateria_inicial", ""))
        if not 0 <= inicial <= 100:
            raise ValueError
    except (TypeError, ValueError):
        inicial = 0
        erros["bateria_inicial"] = "A bateria inicial deve ser um número inteiro entre 0 e 100%."

    try:
        final = int(request.form.get("bateria_final", ""))
        if not 0 <= final <= 100:
            raise ValueError
    except (TypeError, ValueError):
        final = 0
        erros["bateria_final"] = "A porcentagem desejada deve ser um número inteiro entre 0 e 100%."

    if not erros.get("bateria_inicial") and not erros.get("bateria_final") and final <= inicial:
        erros["bateria_final"] = "A porcentagem desejada deve ser maior que a bateria inicial."

    try:
        capacidade = float(request.form.get("capacidade_bateria", ""))
        if not math.isfinite(capacidade) or capacidade <= 0:
            raise ValueError
    except (TypeError, ValueError):
        capacidade = 0
        erros["capacidade_bateria"] = "A capacidade da bateria deve ser maior que zero."

    if any(erros.values()):
        return resposta_com_erros(erros)

    energia = capacidade * (final - inicial) / 100
    with sessoes_lock:
        if placa_ja_cadastrada(placa):
            erros["placa"] = "Já existe uma recarga ou sessão cadastrada para essa placa."
            return resposta_com_erros(erros)
        sessao = criar_sessao(
            placa,
            energia,
            0,
            status="Em andamento",
            bateria_inicial=inicial,
            bateria_final=final,
            capacidade_bateria_kwh=capacidade,
            inicio=time.monotonic(),
        )
        recargas_ativas[sessao.id] = sessao
    return jsonify({
        "sessao_id": sessao.id,
        "status": sessao.status,
        "placa": sessao.placa,
        "bateria_inicial": sessao.bateria_inicial,
        "bateria_final": sessao.bateria_final,
        "capacidade_bateria_kwh": sessao.capacidade_bateria_kwh,
    })


@app.route("/usuario/iniciar-aleatoria", methods=["POST"])
def iniciar_recarga_aleatoria():
    with sessoes_lock:
        placa = gerar_placa_unica()
        if placa is None:
            return jsonify({"erro": "Não foi possível gerar uma placa livre. Tente novamente."}), 503

        capacidade = random.choice([45, 60, 75, 90, 100])
        inicial = random.randint(5, 60)
        final = random.randint(inicial + 3, 100)
        energia = capacidade * (final - inicial) / 100
        sessao = criar_sessao(
            placa,
            energia,
            0,
            status="Em andamento",
            bateria_inicial=inicial,
            bateria_final=final,
            capacidade_bateria_kwh=capacidade,
            inicio=time.monotonic(),
        )
        recargas_ativas[sessao.id] = sessao

    return jsonify({
        "sessao_id": sessao.id,
        "status": sessao.status,
        "placa": sessao.placa,
        "bateria_inicial": sessao.bateria_inicial,
        "bateria_final": sessao.bateria_final,
        "capacidade_bateria_kwh": sessao.capacidade_bateria_kwh,
    })


@app.route("/usuario/finalizar/<int:sessao_id>", methods=["POST"])
def finalizar_recarga_usuario(sessao_id):
    status_solicitado = request.form.get("status", "Concluída")
    status_permitidos = {"Concluída", "Incompleto", "Finalizado antes da hora"}
    if status_solicitado not in status_permitidos:
        return jsonify({"erro": "Status de encerramento inválido."}), 400

    with sessoes_lock:
        sessao = recargas_ativas.pop(sessao_id, None)
        if sessao is None:
            for sessao_salva in sessoes:
                if sessao_salva.id == sessao_id:
                    return jsonify({
                        "status": sessao_salva.status,
                        "tempo_segundos": sessao_salva.tempo_segundos,
                    })
            return jsonify({"erro": "Não há uma recarga ativa com esse registro."}), 404

        sessao.atualizar_tempo(time.monotonic() - sessao.inicio)
        sessao.status = status_solicitado
        sessoes.append(sessao)
    return jsonify({"status": sessao.status, "tempo_segundos": sessao.tempo_segundos})


@app.route("/listar-sessoes")
def listar_sessoes_web():
    mensagem = "Nenhuma sessão cadastrada." if not sessoes else ""
    return render_template("listar_sessoes.html", sessoes=sessoes, mensagem=mensagem)


@app.route("/buscar-sessao", methods=["GET", "POST"])
def buscar_sessao_web():
    sessao = None
    tipo_busca = None
    if request.method == "POST":
        tipo_busca = request.form.get("acao")
        if tipo_busca == "recente":
            # Procura a sessão com o maior ID interno, atribuído na ordem de criação.
            for item in sessoes:
                if sessao is None or item.id > sessao.id:
                    sessao = item
            if sessao is None:
                flash("Ainda não há sessões cadastradas.")
        elif tipo_busca == "especifica":
            placa_busca, erro_placa = validar_placa(request.form.get("placa", ""))
            if erro_placa:
                flash(erro_placa)
            else:
                # Busca sequencial pela placa específica do veículo.
                for item in sessoes:
                    if item.placa == placa_busca:
                        sessao = item
                        break
                if sessao is None:
                    flash("Nenhuma sessão encontrada para essa placa.")
        else:
            flash("Escolha uma forma de busca.")
    return render_template("buscar_sessao.html", sessao=sessao, tipo_busca=tipo_busca)


@app.route("/ordenar-sessoes", methods=["GET", "POST"])
def ordenar_sessoes_web():
    if request.method == "POST":
        n = len(sessoes)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sessoes[j].placa > sessoes[j + 1].placa:
                    sessoes[j], sessoes[j + 1] = sessoes[j + 1], sessoes[j]
        flash("Ordenação manual (Bubble Sort) por placa concluída.")
        return redirect(url_for("ordenar_sessoes_web"))
    return render_template("ordenar_sessoes.html")


@app.route("/estatisticas")
def estatisticas_web():
    return render_template("estatisticas.html", sessoes=sessoes, **obter_estatisticas())


@app.route("/relatorio")
def relatorio_web():
    return render_template("relatorio.html", sessoes=sessoes, **obter_estatisticas())


if __name__ == "__main__":
    app.run(debug=True)
