class Sessao:
    TARIFA_POR_KWH = 0.85

    def __init__(self, id, energia, tempo, status="Em andamento"):
        self.id = id
        self.energia = float(energia)
        self.tempo = int(tempo)
        if self.energia <= 0 or self.tempo <= 0:
            raise ValueError("Energia e tempo devem ser maiores que zero.")

        self.status = status
        self.potencia_media_kw = self.calcular_potencia_media()
        self.custo = self.calcular_custo()

    def calcular_potencia_media(self):
        tempo_em_horas = self.tempo / 60
        return round(self.energia / tempo_em_horas, 2)

    def calcular_custo(self):
        return round(self.energia * self.TARIFA_POR_KWH, 2)