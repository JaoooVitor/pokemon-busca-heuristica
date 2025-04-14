import time
from a_star import a_estrela
from constants import ALCANCE_RADAR, POKEMON_BONUS, INSIGNIAS_POSICOES

class Agente:
    def __init__(self, ambiente):
        self.posicao = ambiente.posicao_inicial
        self.pokemons_capturados = []
        self.insignias_conquistadas = []  # Lista de posições
        self.custo_total = 0
        self.contador_pokemons = {tipo: 0 for tipo in ["agua", "eletrico", "fogo", "voador", "grama"]}
        self.tempo_inicio = time.time()
        self.historico_caminho = []

    def tempo_decorrido(self):
        return time.time() - self.tempo_inicio

    def mover_para(self, destino, ambiente):
        caminho, custo = a_estrela(ambiente.mapa, self.posicao, destino, self.pokemons_capturados)
        self.custo_total += custo
        self.posicao = destino
        self.historico_caminho.extend(caminho)
        return caminho, custo

    def capturar_pokemon(self, posicao, ambiente):
        tipo = ambiente.pokemons_na_posicao[posicao]
        self.pokemons_capturados.append(tipo)
        self.contador_pokemons[tipo] += 1
        del ambiente.pokemons_na_posicao[posicao]

    def conquistar_insignia(self, posicao):
        if posicao in INSIGNIAS_POSICOES and posicao not in self.insignias_conquistadas:
            self.insignias_conquistadas.append(posicao)

    def decidir_proxima_acao(self, ambiente, pokemons_visiveis):
        ginasios = ambiente.ginasios
        posicao = self.posicao

        proximo_ginasio = (
            min(ginasios, key=lambda g: abs(posicao[0] - g[0]) + abs(posicao[1] - g[1]))
            if ginasios else None
        )

        pokemons_uteis = [
            p for p in pokemons_visiveis
            if self._pokemon_eh_util(ambiente, p)
        ]

        proximo_pokemon = (
            min(pokemons_uteis, key=lambda p: abs(posicao[0] - p[0]) + abs(posicao[1] - p[1]))
            if pokemons_uteis else None
        )

        dist_ginasio = abs(posicao[0] - proximo_ginasio[0]) + abs(posicao[1] - proximo_ginasio[1]) if proximo_ginasio else float('inf')
        dist_pokemon = abs(posicao[0] - proximo_pokemon[0]) + abs(posicao[1] - proximo_pokemon[1]) if proximo_pokemon else float('inf')

        if proximo_ginasio and (dist_ginasio <= dist_pokemon + 3):
            return proximo_ginasio, "ginasio"

        if proximo_pokemon:
            return proximo_pokemon, "pokemon"

        return None, "fim"

    def _pokemon_eh_util(self, ambiente, posicao_pokemon):
        tipo = ambiente.pokemons_na_posicao[posicao_pokemon]

        # Garantir pelo menos um de cada tipo
        if self.contador_pokemons[tipo] == 0:
            print(f"🧠 Ainda não temos nenhum {tipo}. Considerado útil!")
            return True

        terrenos_necessarios = set(
            ambiente.get_terreno(g)
            for g in ambiente.ginasios
        )

        print(f"🧠 Analisando: {tipo} | Terrenos necessários: {terrenos_necessarios}")

        for terreno in terrenos_necessarios:
            if terreno in POKEMON_BONUS.get(tipo, {}):
                print(f"✅ {tipo} é útil para {terreno}")
                return True

        print(f"❌ {tipo} não é útil no momento.")
        return False
