class Sessao:
    TARIFA_POR_KWH = 0.85

    def __init__(
        self,
        placa,
        energia,
        tempo_segundos,
        status="Concluída",
        bateria_inicial=None,
        bateria_final=None,
        capacidade_bateria_kwh=None,
        inicio=None,
    ):
        self.placa = placa.strip().upper()
        self.energia = float(energia)
        self.tempo_segundos = int(tempo_segundos)
        self.tempo = max(1, round(self.tempo_segundos / 60))
        if self.energia <= 0 or self.tempo_segundos < 0:
            raise ValueError("Energia deve ser maior que zero e o tempo não pode ser negativo.")

        self.status = status
        self.bateria_inicial = bateria_inicial
        self.bateria_final = bateria_final
        self.capacidade_bateria_kwh = capacidade_bateria_kwh
        self.inicio = inicio
        self.potencia_media_kw = self.calcular_potencia_media()
        self.custo = self.calcular_custo()

    def calcular_potencia_media(self):
        if self.tempo_segundos <= 0:
            return 0
        tempo_em_horas = self.tempo_segundos / 3600
        return round(self.energia / tempo_em_horas, 2)

    def calcular_custo(self):
        return round(self.energia * self.TARIFA_POR_KWH, 2)

    def atualizar_tempo(self, tempo_segundos):
        self.tempo_segundos = max(1, round(float(tempo_segundos)))
        self.tempo = max(1, round(self.tempo_segundos / 60))
        self.potencia_media_kw = self.calcular_potencia_media()
