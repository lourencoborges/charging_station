



def main_lobby():
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



escolha = main_lobby()



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
    if escolha == 1:
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
        
        
        sessoes.append(Sessao(id, energia, tempo, custo))




cadastro = cadastrar_sessao()




def listar_sessoes():
    if escolha == 2:
        print("==================")
        print("      LISTA       ")
        print("==================")
        for sessao in sessoes:
            print("ID: ", sessao.id)
            print("Energia: ", sessao.energia)
            print("Tempo: ", sessao.tempo)
            print("Custo: ", sessao.custo)
            print("")
            


listar_sessoes()


def buscar_sessao():
    if escolha == 3:
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


buscar_sessao()



def ordenar_sessoes():
    if escolha == 4:
        for i in range(len(sessoes)):
            for sessao in range(len(sessoes) - 1):
                if sessoes[sessao].id > sessoes[sessao + 1].id:
                    sessoes[sessao], sessoes[sessao + 1] = sessoes[sessao + 1], sessoes[sessao]
        print("Sessões ordenadas com sucesso")


ordenar_sessoes()

def mostrar_estatisticas():
    
    if escolha == 5:
        #conta quantas sessoes tem
        contagem_sessao = len(sessoes)

        #esse codigo consegue ve o total de energia que a lsita(sessoes) tem,
        #quanto de dinheiro tem na lista
        total_receita = 0
        total_energia = 0
        for sessao in sessoes:
            total_energia += sessao.energia
            total_receita += sessao.custo

        #verifica se existe receita ou uma lista para não ocorrer uma divisão por 0
        if contagem_sessao == 0:
            print()
            print("Erro, nao existe receita ou uma sessão")
            return
        else:
            #esse vai calcular o custo medio das sessoes
            custo_medio = total_receita / contagem_sessao


        print()
        print("========================================")
        print("         ESTATISTÍCAS                   ")
        print()
        print("Sessões existentes:", contagem_sessao)
        print("Total de energia: ", total_energia)
        print("Receita total: ", total_receita)
        print("O custo medio é: ", round(custo_medio, 2))
        print("========================================")

mostrar_estatisticas()
        