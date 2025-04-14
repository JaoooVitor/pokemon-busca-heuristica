# environment.py

import random
from constants import CUSTO_TERRENO, POKEMON_BONUS, QUANTIDADE_POKEMONS, TAMANHO_MAPA

class Ambiente:
    def __init__(self):
        self.mapa = self.gerar_mapa()
        self.posicao_inicial = (19, 24)  # Laboratório do Professor Carvalho
        from constants import INSIGNIAS_POSICOES
        self.ginasios = list(INSIGNIAS_POSICOES.keys())
        self.pokemons_na_posicao = self.sortear_pokemons()

    def gerar_mapa(self):
        """Mapa hardcoded com 42x42 células."""
        return [
            list("MGGGGMGAGGGGGGGGMMMMMMMGGGMMMMMGGGGMMMGGGG"),
            list("MGMMMMGAGMMMMGGMMMMMMMMMGGMGGGMGGMMMMMMMGG"),
            list("MGGGGMGAGMGGMGMMMMMMMMMMMGMMGMMGMMMMVMMMMG"),
            list("MGMMMMGAGMGGMGMMMMMMMMMMMGGMGMGMMMMVVVMMMM"),
            list("MGGGGMGAGGGGGGGMMMMMMMMMGGGMGMGMMMVVVVVMMM"),
            list("MMMMGMGAAAAAGGGGGMMMMMGGGMGMGMGMMMMVVVMMMM"),
            list("GMGGGGGGGGGAGMMGGGGGGGGGGMGMGMGGMMMMVMMMMG"),
            list("GMGGGGMMMMGAGMMGGGGMGGMGGGGGGGGGGMMMMMMMGG"),
            list("GGGGMGGGGGGGGGGGGGMMMGGGMMMMMMMGGGGMMMGGGG"),
            list("GGMGGGGGMMGAGMMGMGGMGGGGGGGGGGGGGGGGGGGGMG"),
            list("GGMGMMMGMMGAGMMGMGGGGGGGMMMGGGMMMGMMMMGGMG"),
            list("GGMGGGGGGGGAGGGGMMMMMGGMMMMMGGMMMGGGGGGGGG"),
            list("GGMGGGGGGGGAAAAGMGGMGGMMMMMMMGGGGGMGGMMMMG"),
            list("GGGGGGGGMGGGGGAGMGGMGGMMMAMMMGGGGGMGGGGGGG"),
            list("MMMMGMGMMMGGGGAGGGGMGGGMMAMMGGGGMMMMMMMGGG"),
            list("GGGGGMGMMMGGAAAAAGGMGGGGGAGGGGGGGGGMGGGGGG"),
            list("GGMGGMGGMGGAAAAAAAGGGMMMGAGGGMGGMGGMGGGGGG"),
            list("MGMGGMGGGGAAAAAAAAAGGGGGGAGMMMMGMGGMGGGGMM"),
            list("MGMGGMGGGGAAAGGGAAAGGMGGGAGGGMGGMGGGGMMMMM"),
            list("MGMGMMMGGGAAAGGGAAAGMMMGGAGGGGGGMMMGMMMMMM"),
            list("MGGGGGGGGGAAAGGGAAAGMMMGGAAAAAAGGGGGGGGGMM"),
            list("MMMMMGGGGGAAAAAAAAAGMMMGGGGGGGAGMMMGMMMMMM"),
            list("GGGGMGMGGGGAAAAAAAGGGMGGGMMMGGAGMGGGGMMMMM"),
            list("GGGGMGMGGGGGAAAAAGGGGGGGGMMMGGAGMGMMGGGGMM"),
            list("GGMGGGMGMMGGGGAGGGGGGMMMGGGGGGAGMGMGGGGGGG"),
            list("GMMMGGMGMMMMGGAGGGMMGGGGGGMGGGAGGGMMMMGGGG"),
            list("GMMMGMMGGGGGGGAGGMMMMGGGMGMGGAAAGGGMMMGGMG"),
            list("GMMMGGGGMMMGGGAGMMMMMMGGMGGGAAAAAGGGGGGGMG"),
            list("GGMGGGGGGGGGGGAGMMMMMMGGMGGAAAAAAAGGMMMMMG"),
            list("MGGGMGGMAAAAAAAGGMMMMGGGMGGGAAAAAGGGMGGGMG"),
            list("MMGMMMGGAGGGGGMGGGMMGGMMMMGGGAAAGGGGGGGGGG"),
            list("MMGMMMGGAGGGGGMGMGGGGGGGGGGGGGGGGMMMMGMMMG"),
            list("MGGGMGGGAGMMMMMGMMMMGMMMMMMGGGGMGGGMGGGMGG"),
            list("GGGGGGGGGGGGGGGGGGGGGGGGGGMGGMMMMMGMGMGMGM"),
            list("GMGMMMMGAGMMMGMMMMMMMMMMGMMGGGGGGGGGGGGMGM"),
            list("GMGGGGMGAGGMGGMGGGGGGGGMGMGGMMMMCMMMMGGMGM"),
            list("GMMMGGMGAGGMGGMGMMMMMMGMGGGMMMVVCVVMMMGGGM"),
            list("GMGGGGMGAGGGGGMGMGGGGMGMGGMMVVVVCVVVVMMGGM"),
            list("MMGMMMMGAAAAGGMGGGGGGMGMGGMMVVVVCVVVVMMGGG"),
            list("MGGGGGMGGGGAGGMMMMMMMMGMGMMVVVVVCVVVVVMMGG"),
            list("MGMMMGMGGGGAGGGGGGGGGGGGGMMVVVVVCVVVVVMMGG"),
            list("MGGGGGMGGGGAGGMMMMMMMMMMGMMVVVVVVVVVVVMMGG"),
        ]

    def sortear_pokemons(self):
        """Sorteia pokémons nas regiões de grama."""
        pokemons = []
        for tipo, qtd in QUANTIDADE_POKEMONS.items():
            pokemons += [tipo] * qtd

        random.shuffle(pokemons)

        posicoes_validas = [
            (i, j)
            for i in range(TAMANHO_MAPA)
            for j in range(TAMANHO_MAPA)
            if self.mapa[i][j] == "G"
        ]

        random.shuffle(posicoes_validas)
        return dict(zip(posicoes_validas[: len(pokemons)], pokemons))

    def get_terreno(self, pos):
        x, y = pos
        return self.mapa[x][y]

    def radar_pokedex(self, posicao, alcance=4):
        """Retorna pokémons no alcance do radar."""
        x, y = posicao
        return [
            p for p in self.pokemons_na_posicao
            if abs(p[0] - x) <= alcance and abs(p[1] - y) <= alcance
        ]
